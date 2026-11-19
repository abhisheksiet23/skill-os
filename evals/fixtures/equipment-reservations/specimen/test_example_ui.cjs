"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { spawn } = require("node:child_process");
const readline = require("node:readline");
const { chromium } = require(process.env.ER1_PLAYWRIGHT_MODULE || "playwright");

const python = process.env.ER1_PYTHON || "python";
const artifactDirectory = path.resolve(
  process.env.ER1_ARTIFACT_DIR || path.join(__dirname, "../../../../.eval-runs/er1-t10"),
);
fs.mkdirSync(artifactDirectory, { recursive: true });

async function launchExample() {
  const server = spawn(python, ["-B", path.join(__dirname, "example_server.py")], {
    windowsHide: true,
    stdio: ["ignore", "pipe", "pipe"],
  });
  const lines = readline.createInterface({ input: server.stdout });
  let stderr = "";
  server.stderr.on("data", (chunk) => { stderr += chunk.toString(); });
  try {
    const url = await new Promise((resolve, reject) => {
      const timeout = setTimeout(() => reject(new Error(`Server readiness timeout: ${stderr}`)), 10000);
      lines.on("line", (line) => {
        if (line.startsWith("ER1_URL=")) {
          clearTimeout(timeout);
          resolve(line.slice("ER1_URL=".length));
        }
      });
      server.once("error", (error) => { clearTimeout(timeout); reject(error); });
      server.once("exit", (code) => { clearTimeout(timeout); reject(new Error(`Server exit ${code}: ${stderr}`)); });
    });
    return { server, lines, url };
  } catch (error) {
    server.kill();
    lines.close();
    throw error;
  }
}

async function run() {
  const browser = await chromium.launch({ headless: true });
  console.log(`Environment: Node ${process.version}; Chromium ${browser.version()}`);
  let passed = 0;

  async function example(name, viewport, test) {
    const local = await launchExample();
    const context = await browser.newContext({ viewport, baseURL: local.url });
    const page = await context.newPage();
    const requests = [];
    const errors = [];
    page.on("request", (request) => {
      if (request.method() === "POST" && request.url().endsWith("/api/confirm")) {
        requests.push(request.postDataJSON());
      }
    });
    page.on("pageerror", (error) => errors.push(error.message));
    try {
      await page.goto(local.url);
      await page.locator("#confirm").waitFor({ state: "visible" });
      await page.waitForFunction(() => !document.querySelector("#confirm").disabled);
      assert.equal(requests.length, 0, "Loading must not submit a reservation");
      await test({ page, requests, context, url: local.url });
      assert.deepEqual(errors, [], "Browser runtime errors");
      passed += 1;
      console.log(`PASS: ${name}`);
    } finally {
      await context.close();
      local.server.kill();
      local.lines.close();
    }
  }

  async function conflict(page) {
    await page.getByRole("button", { name: "Confirm reservation" }).click();
    await page.getByText("This equipment is already booked.", { exact: true }).waitFor();
    assert.equal(await page.locator("#asset").inputValue(), "REC-01");
    assert.equal(await page.locator("#start").inputValue(), "2026-11-20");
    assert.equal(await page.locator("#end").inputValue(), "2026-11-21");
    assert.equal(await page.evaluate(() => document.activeElement.id), "notice");
    assert.equal(await page.locator(".confirmation").count(), 0);
  }

  try {
    for (const width of [1280, 768, 360]) {
      await example(`conflict retains draft and reflows at ${width}px`, { width, height: 900 }, async ({ page, requests }) => {
        await conflict(page);
        assert.equal(requests.length, 1);
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
        for (const id of ["asset", "start", "end", "confirm"]) {
          const bounds = await page.locator(`#${id}`).boundingBox();
          assert.ok(bounds.x >= 0 && bounds.x + bounds.width <= width);
        }
        await page.screenshot({ path: path.join(artifactDirectory, `conflict-${width}.png`), fullPage: true });
      });
    }

    await example("typed dates survive conflict without reverting to defaults", { width: 768, height: 900 }, async ({ page, requests }) => {
      await page.locator("#start").fill("2026-11-19");
      await page.locator("#end").fill("2026-11-20");
      await page.getByRole("button", { name: "Confirm reservation" }).click();
      await page.getByText("This equipment is already booked.", { exact: true }).waitFor();
      assert.equal(await page.locator("#asset").inputValue(), "REC-01");
      assert.equal(await page.locator("#start").inputValue(), "2026-11-19");
      assert.equal(await page.locator("#end").inputValue(), "2026-11-20");
      assert.equal(requests.length, 1);
    });

    await example("alternative selection requires explicit confirmation", { width: 1280, height: 900 }, async ({ page, requests }) => {
      await conflict(page);
      await page.getByRole("button", { name: "Choose another asset" }).click();
      assert.equal(await page.evaluate(() => document.activeElement.id), "asset");
      await page.locator("#asset").selectOption("PROJ-01");
      assert.equal(await page.locator("#start").inputValue(), "2026-11-20");
      assert.equal(await page.locator("#end").inputValue(), "2026-11-21");
      assert.match(await page.locator("#draft-status").textContent(), /Nothing submitted/);
      const before = await (await page.request.get("/api/reservations")).json();
      assert.equal(before.confirmations.length, 0);
      assert.equal(requests.length, 1);
      await page.getByRole("button", { name: "Confirm reservation" }).click();
      await page.getByText("Your reservation is confirmed.", { exact: true }).waitFor();
      await page.locator(".confirmation").waitFor();
      assert.equal(requests.length, 2);
      assert.notEqual(requests[0].operation_id, requests[1].operation_id);
      assert.match(await page.locator(".confirmation").textContent(), /Projector/);
      await page.screenshot({ path: path.join(artifactDirectory, "confirmed-1280.png"), fullPage: true });
    });

    await example("keyboard edit preserves asset and does not autosubmit", { width: 768, height: 900 }, async ({ page, requests }) => {
      await conflict(page);
      await page.getByRole("button", { name: "Edit dates" }).focus();
      await page.keyboard.press("Enter");
      assert.equal(await page.evaluate(() => document.activeElement.id), "start");
      await page.locator("#start").fill("2026-11-22");
      await page.locator("#end").fill("2026-11-23");
      assert.equal(requests.length, 1);
      assert.equal(await page.locator("#asset").inputValue(), "REC-01");
      await page.getByRole("button", { name: "Confirm reservation" }).focus();
      await page.keyboard.press("Enter");
      await page.getByText("Your reservation is confirmed.", { exact: true }).waitFor();
      assert.equal(requests.length, 2);
    });

    await example("pending requests suppress repeated submit events", { width: 1280, height: 900 }, async ({ page, requests }) => {
      await page.locator("#asset").selectOption("PROJ-01");
      let release;
      let entered;
      const gate = new Promise((resolve) => { release = resolve; });
      const started = new Promise((resolve) => { entered = resolve; });
      await page.route("**/api/confirm", async (route) => {
        entered();
        await gate;
        await route.continue();
      });
      await page.getByRole("button", { name: "Confirm reservation" }).click();
      await started;
      assert.equal(await page.locator("#confirm").isDisabled(), true);
      await page.evaluate(() => document.querySelector("form").requestSubmit());
      assert.equal(requests.length, 1);
      release();
      await page.getByText("Your reservation is confirmed.", { exact: true }).waitFor();
      const result = await (await page.request.get("/api/reservations")).json();
      assert.equal(result.confirmations.length, 1);
    });

    await example("accepted then lost response recovers only on explicit retry", { width: 1280, height: 900 }, async ({ page, requests }) => {
      await page.locator("#asset").selectOption("PROJ-01");
      let first = true;
      await page.route("**/api/confirm", async (route) => {
        if (first) {
          first = false;
          await route.fetch();
          await route.abort("failed");
        } else {
          await route.continue();
        }
      });
      await page.getByRole("button", { name: "Confirm reservation" }).click();
      await page.getByText("We couldn’t confirm the result.", { exact: true }).waitFor();
      assert.equal(requests.length, 1);
      assert.equal(await page.locator("#asset").isDisabled(), true);
      await page.getByRole("button", { name: "Check confirmation", exact: true }).click();
      await page.getByText("Your reservation is confirmed.", { exact: true }).waitFor();
      assert.equal(requests.length, 2);
      assert.deepEqual(requests[0], requests[1]);
      const result = await (await page.request.get("/api/reservations")).json();
      assert.equal(result.confirmations.length, 1);
      assert.equal(await page.locator("#asset").isDisabled(), false);
    });

    await example("server rejects four-day projector draft without clearing it", { width: 360, height: 900 }, async ({ page, requests }) => {
      await page.locator("#asset").selectOption("PROJ-01");
      await page.locator("#start").fill("2026-11-22");
      await page.locator("#end").fill("2026-11-25");
      assert.match(await page.locator("#asset-help").textContent(), /Up to 3 days/);
      await page.getByRole("button", { name: "Confirm reservation" }).click();
      await page.getByText("This reservation could not be confirmed.", { exact: true }).waitFor();
      assert.equal(await page.locator("#end").inputValue(), "2026-11-25");
      assert.equal(requests.length, 1);
      assert.equal(await page.locator(".confirmation").count(), 0);
    });
  } finally {
    await browser.close();
  }
  console.log(`PASS: ${passed} browser scenarios; screenshots: ${artifactDirectory}`);
}

run().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
