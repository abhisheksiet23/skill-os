"use strict";

const form = document.querySelector("#reservation-form");
const fields = document.querySelector("#draft-fields");
const asset = document.querySelector("#asset");
const start = document.querySelector("#start");
const end = document.querySelector("#end");
const confirmButton = document.querySelector("#confirm");
const notice = document.querySelector("#notice");
const noticeTitle = document.querySelector("#notice-title");
const noticeBody = document.querySelector("#notice-body");
const recoveryActions = document.querySelector("#conflict-actions");
const status = document.querySelector("#draft-status");
const limits = {};
const labels = { "REC-01": "Recorder", "CAM-01": "Camera", "PROJ-01": "Projector" };
let pendingOperation = null;
let busy = false;
let uncertain = false;
let ready = false;

function currentDraft() {
  return { asset_id: asset.value, start: start.value, end: end.value };
}

function updateSummary() {
  const duration = Math.round((Date.parse(end.value) - Date.parse(start.value)) / 86400000) + 1;
  const days = Number.isFinite(duration) && duration > 0
    ? `${duration} calendar ${duration === 1 ? "day" : "days"}`
    : "Choose valid dates";
  document.querySelector("#draft-summary").textContent = `${labels[asset.value]} · ${days}`;
  document.querySelector("#asset-help").textContent = `Up to ${limits[asset.value]} days. Dates include weekends.${asset.value === "CAM-01" ? " Current camera training required." : ""}`;
  end.setCustomValidity(end.value < start.value ? "End date cannot be before start date." : "");
}

function showNotice(title, body, kind = "error", conflict = false) {
  noticeTitle.textContent = title;
  noticeBody.textContent = body;
  notice.className = kind === "success" ? "notice success" : "notice";
  recoveryActions.hidden = !conflict;
  notice.hidden = false;
  notice.focus();
}

function updateControls() {
  fields.disabled = !ready || busy || uncertain;
  confirmButton.disabled = !ready || busy;
  confirmButton.textContent = busy ? "Checking availability…" : uncertain ? "Check confirmation" : "Confirm reservation →";
  form.setAttribute("aria-busy", String(busy));
}

function renderConfirmations(confirmations) {
  const container = document.querySelector("#confirmations");
  container.replaceChildren();
  if (confirmations.length === 0) {
    const mark = document.createElement("div");
    mark.className = "empty-mark";
    mark.setAttribute("aria-hidden", "true");
    mark.textContent = "↗";
    const title = document.createElement("p");
    title.className = "empty-title";
    title.textContent = "No reservations yet";
    const description = document.createElement("p");
    description.className = "muted";
    description.textContent = "Once confirmed, your equipment and confirmation reference will appear here.";
    container.append(mark, title, description);
    return;
  }

  for (const confirmation of confirmations) {
    const item = document.createElement("div");
    item.className = "confirmation";
    const name = document.createElement("strong");
    name.textContent = confirmation.asset_label;
    const dates = document.createElement("p");
    dates.textContent = `${confirmation.start} to ${confirmation.end}`;
    const reference = document.createElement("p");
    reference.className = "reference";
    reference.textContent = confirmation.reference;
    item.append(name, dates, reference);
    container.append(item);
  }
}

async function loadConfirmations() {
  const response = await fetch("/api/reservations");
  if (!response.ok) {
    throw new Error("Could not load confirmations");
  }
  const data = await response.json();
  renderConfirmations(data.confirmations);
}

function draftChanged() {
  if (busy || uncertain) {
    return;
  }
  pendingOperation = null;
  notice.hidden = true;
  status.textContent = "Draft updated. Nothing submitted. Confirm when ready.";
  updateSummary();
}

asset.addEventListener("change", draftChanged);
start.addEventListener("input", draftChanged);
end.addEventListener("input", draftChanged);
document.querySelector("#choose-asset").addEventListener("click", () => asset.focus());
document.querySelector("#edit-dates").addEventListener("click", () => start.focus());

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!ready || busy) {
    return;
  }
  if (!uncertain && !form.reportValidity()) {
    return;
  }

  pendingOperation ??= { operation_id: crypto.randomUUID(), ...currentDraft() };
  busy = true;
  updateControls();
  status.textContent = uncertain ? "Checking your previous confirmation…" : "Checking current availability…";

  try {
    const response = await fetch("/api/confirm", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(pendingOperation),
    });
    const result = await response.json();
    if (response.status >= 500) {
      throw new Error("Uncertain server outcome");
    }

    uncertain = false;
    pendingOperation = null;
    if (response.ok) {
      showNotice("Your reservation is confirmed.", `${result.asset_label} is reserved from ${result.start} to ${result.end}. Reference ${result.reference}.`, "success");
      status.textContent = "Confirmed. Your reservation appears on the right or below.";
      try {
        await loadConfirmations();
      } catch {
        status.textContent = `Confirmed: ${result.reference}. The list could not refresh; reload to view your confirmations.`;
      }
    } else if (result.code === "availability_conflict") {
      showNotice("This equipment is already booked.", "No reservation was created. Your equipment selection and dates are still here. Choose another asset or edit the dates, then confirm again.", "error", true);
      status.textContent = "Draft kept. Changes won’t submit automatically.";
    } else {
      showNotice("This reservation could not be confirmed.", "Check the dates, duration and training requirements. Your entered details are still here.");
      status.textContent = "Nothing confirmed. Review the details before trying again.";
    }
  } catch {
    uncertain = true;
    showNotice("We couldn’t confirm the result.", "Your request may have been accepted. Choose Check confirmation to recover the same request before changing its details.");
    status.textContent = "No automatic retry. Check confirmation when ready.";
  } finally {
    busy = false;
    updateControls();
  }
});

async function initialize() {
  try {
    const [catalogue] = await Promise.all([fetch("/api/catalogue").then((response) => {
      if (!response.ok) {
        throw new Error("Catalogue unavailable");
      }
      return response.json();
    }), loadConfirmations()]);
    for (const item of catalogue.assets) {
      limits[item.identifier] = item.maximum_days;
      labels[item.identifier] = item.label;
    }
    updateSummary();
    ready = true;
    status.textContent = "Nothing submitted. Confirm when ready.";
  } catch {
    showNotice("The equipment desk is unavailable.", "Reload to try loading this local example again. No confirmation request was sent.");
    status.textContent = "Service unavailable. Confirmation is disabled.";
  }
  updateControls();
}

initialize();
