"""Real loopback HTTP checks for the synthetic rendered-state example."""

from http.client import HTTPConnection
import json
from threading import Thread
import unittest

from example_server import create_server


class ExampleHttpContract(unittest.TestCase):
    def setUp(self):
        self.server = create_server()
        self.thread = Thread(
            target=lambda: self.server.serve_forever(poll_interval=0.01),
            daemon=True,
        )
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def send(self, method, path, body=None, headers=None):
        connection = HTTPConnection("127.0.0.1", self.server.server_port, timeout=3)
        try:
            connection.request(method, path, body=body, headers=headers or {})
            response = connection.getresponse()
            return response.status, response.getheader("Content-Type"), response.read()
        finally:
            connection.close()

    def confirm(self, asset="REC-01", start="2026-11-20", end="2026-11-21", operation="OP-UI"):
        payload = {"operation_id": operation, "asset_id": asset, "start": start, "end": end}
        status, _, body = self.send(
            "POST", "/api/confirm", json.dumps(payload), {"Content-Type": "application/json"}
        )
        return status, json.loads(body)

    def test_static_example_and_catalogue_use_actual_policy(self):
        for path in ("/", "/example.css", "/example.js"):
            status, _, body = self.send("GET", path)
            self.assertEqual(200, status)
            self.assertTrue(body)

        status, _, body = self.send("GET", "/api/catalogue")
        self.assertEqual(200, status)
        policies = {item["kind"]: item["maximum_days"] for item in json.loads(body)["assets"]}
        self.assertEqual({"recorder": 7, "camera": 3, "projector": 3}, policies)

    def test_conflict_does_not_disclose_seed_owner_or_create_confirmation(self):
        status, body = self.confirm()
        self.assertEqual(409, status)
        self.assertEqual({"code": "availability_conflict"}, body)
        status, _, own = self.send("GET", "/api/reservations")
        self.assertEqual(200, status)
        self.assertEqual({"confirmations": []}, json.loads(own))

    def test_explicit_alternative_confirms_once_and_replays(self):
        self.assertEqual(409, self.confirm()[0])
        accepted, first = self.confirm(asset="PROJ-01", operation="ALTERNATIVE")
        replayed, second = self.confirm(asset="PROJ-01", operation="ALTERNATIVE")
        self.assertEqual((200, 200), (accepted, replayed))
        self.assertEqual(first, second)
        status, _, body = self.send("GET", "/api/reservations")
        self.assertEqual(200, status)
        self.assertEqual([first], json.loads(body)["confirmations"])

    def test_real_http_honors_er_limit(self):
        self.assertEqual(200, self.confirm("PROJ-01", "2026-11-18", "2026-11-20")[0])
        self.assertEqual(400, self.confirm("PROJ-01", "2026-11-22", "2026-11-25", "TOO-LONG")[0])

    def test_malformed_payload_and_forged_employee_rejected(self):
        for payload in (
            None,
            [],
            {"employee_id": "EMP-02"},
            {"operation_id": "X", "asset_id": "REC-01", "start": True, "end": "2026-11-21"},
        ):
            status, _, _ = self.send(
                "POST", "/api/confirm", json.dumps(payload), {"Content-Type": "application/json"}
            )
            self.assertEqual(400, status)

    def test_cross_origin_and_static_traversal_denied(self):
        status, _, _ = self.send(
            "POST", "/api/confirm", "{}",
            {"Content-Type": "application/json", "Origin": "https://example.invalid"},
        )
        self.assertEqual(403, status)
        self.assertEqual(404, self.send("GET", "/../../reservations.py")[0])
        self.assertEqual(415, self.send("POST", "/api/confirm", "{}")[0])


if __name__ == "__main__":
    unittest.main()
