"""Loopback-only ER-1 example adapter; trusted employee and synthetic clock."""

import argparse
from dataclasses import asdict
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from urllib.parse import urlsplit

from reservations import (
    ASSET_POLICIES,
    AccessDenied,
    ConfirmationRequest,
    InvalidRequest,
    ReservationConflict,
    Reservations,
)


ASSET_LABELS = {"REC-01": "Recorder", "CAM-01": "Camera", "PROJ-01": "Projector"}
STATIC_FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/example.css": ("example.css", "text/css; charset=utf-8"),
    "/example.js": ("example.js", "text/javascript; charset=utf-8"),
}


def confirmation_json(confirmation):
    return {
        "reference": confirmation.reference,
        "asset_id": confirmation.request.asset_id,
        "asset_label": ASSET_LABELS[confirmation.request.asset_id],
        "start": confirmation.request.start.isoformat(),
        "end": confirmation.request.end.isoformat(),
    }


def create_server(port=0):
    service = Reservations(lambda: date(2026, 11, 18))
    static_root = Path(__file__).parent / "web"

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            pass

        def send_json(self, status, body):
            encoded = json.dumps(body).encode("utf-8")
            self.send_bytes(status, encoded, "application/json; charset=utf-8")

        def send_bytes(self, status, body, content_type):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            path = urlsplit(self.path).path
            if path == "/api/catalogue":
                assets = [
                    {
                        **asdict(asset),
                        "label": ASSET_LABELS[asset.identifier],
                        "maximum_days": ASSET_POLICIES[asset.kind].maximum_days,
                        "requires_camera_training": ASSET_POLICIES[asset.kind].requires_camera_training,
                    }
                    for asset in service.catalogue("EMP-01")
                ]
                self.send_json(200, {"assets": assets, "today": "2026-11-18"})
            elif path == "/api/reservations":
                own = service.own_confirmations("EMP-01")
                self.send_json(200, {"confirmations": [confirmation_json(c) for c in own]})
            elif path in STATIC_FILES:
                name, mime = STATIC_FILES[path]
                self.send_bytes(200, (static_root / name).read_bytes(), mime)
            else:
                self.send_json(404, {"code": "not_found"})

        def do_POST(self):
            if self.path != "/api/confirm":
                self.send_json(404, {"code": "not_found"})
                return

            origin = self.headers.get("Origin")
            expected_origin = f"http://127.0.0.1:{self.server.server_port}"
            if origin is not None and origin != expected_origin:
                self.send_json(403, {"code": "access_denied"})
                return

            if self.headers.get_content_type() != "application/json":
                self.send_json(415, {"code": "invalid_content_type"})
                return

            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 4096:
                    raise ValueError("Invalid request size")

                payload = json.loads(self.rfile.read(length))
                if type(payload) is not dict or set(payload) != {
                    "operation_id", "asset_id", "start", "end"
                }:
                    raise ValueError("Invalid request shape")

                # Accept exact ISO date strings; do not silently normalize them.
                for field in ("start", "end"):
                    value = payload[field]
                    if type(value) is not str or date.fromisoformat(value).isoformat() != value:
                        raise ValueError("Invalid date")

                request = ConfirmationRequest(
                    operation_id=payload["operation_id"],
                    asset_id=payload["asset_id"],
                    start=date.fromisoformat(payload["start"]),
                    end=date.fromisoformat(payload["end"]),
                )
            except (ValueError, TypeError, UnicodeError):
                self.send_json(400, {"code": "invalid_request"})
                return

            try:
                result = service.confirm("EMP-01", request)
            except ReservationConflict as error:
                code = (
                    "availability_conflict"
                    if str(error) == "Asset unavailable for those dates"
                    else "operation_conflict"
                )
                self.send_json(409, {"code": code})
            except AccessDenied:
                self.send_json(403, {"code": "access_denied"})
            except InvalidRequest:
                self.send_json(400, {"code": "invalid_request"})
            else:
                self.send_json(200, confirmation_json(result))

    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=0)
    args = parser.parse_args()
    server = create_server(args.port)
    print(f"ER1_URL=http://127.0.0.1:{server.server_port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
