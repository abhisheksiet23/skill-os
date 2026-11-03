"""Local external-boundary simulator for isolated skill evaluations.

Calls: Client(output_directory), login("operator-session"), launch_worker(),
create_draft(name, worker), read_back(name). No credentials or network required.
The operator-session reference is supplied by the fixture host. Never pass a
password. The dependency is fixed input; performers must not modify this file.
"""

import json
import time
from pathlib import Path


class Client:
    def __init__(self, output_directory):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)
        self.authenticated = False

    def _record(self, operation, **fields):
        event = {"time_ns": time.time_ns(), "operation": operation, **fields}
        with (self.output_directory / "dependency-events.jsonl").open(
            "a", encoding="utf-8"
        ) as stream:
            stream.write(json.dumps(event) + "\n")

    def login(self, secret_reference):
        success = secret_reference == "operator-session"
        self._record("login", success=success)
        self.authenticated = success
        return {"authenticated": success}

    def launch_worker(self):
        self._record("launch_worker", identity="fixture-worker")
        return {"identity": "fixture-worker"}

    def create_draft(self, name, worker):
        if not self.authenticated:
            self._record("create_denied", reason="unauthenticated")
            return {"status": 401, "outcome": "denied"}
        if not name.startswith("AUTO_") or worker != {"identity": "fixture-worker"}:
            self._record("create_denied", reason="ownership-or-worker")
            return {"status": 403, "outcome": "denied"}
        self._record("create_attempt", name=name, outcome="unknown")
        return {
            "status": 500,
            "outcome": "unknown",
            "message": "Draft service failed; persistence outcome unavailable.",
        }

    def read_back(self, name):
        self._record("read_back", name=name)
        return {"status": 503, "outcome": "unavailable"}
