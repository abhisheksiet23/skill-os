"""ER-1 synthetic, single-process specimen with shared asset reservation rules."""

from dataclasses import dataclass
from datetime import date
from threading import RLock
from types import MappingProxyType
from typing import Callable


class InvalidRequest(ValueError):
    pass


class AccessDenied(PermissionError):
    pass


class ReservationConflict(ValueError):
    pass


@dataclass(frozen=True)
class ReservationPolicy:
    maximum_days: int
    requires_camera_training: bool = False

    def validate(self, duration: int, camera_training_current: bool) -> None:
        if duration > self.maximum_days:
            raise InvalidRequest("Reservation exceeds asset duration limit")

        if self.requires_camera_training and not camera_training_current:
            raise AccessDenied("Current camera training required")


ASSET_POLICIES = MappingProxyType({
    "recorder": ReservationPolicy(maximum_days=7),
    "camera": ReservationPolicy(maximum_days=3, requires_camera_training=True),
    "projector": ReservationPolicy(maximum_days=3),
})


@dataclass(frozen=True)
class Asset:
    identifier: str
    kind: str


@dataclass(frozen=True)
class ConfirmationRequest:
    operation_id: str
    asset_id: str
    start: date
    end: date


@dataclass(frozen=True)
class Confirmation:
    reference: str
    employee_id: str
    request: ConfirmationRequest


class Reservations:
    """Caller identity is supplied by the trusted host, never by a request body.

    One lock covers all reads/writes in this instance. There is no persistence,
    multi-process coordination, token validation or HTTP boundary in this slice.
    """

    def __init__(self, office_today: Callable[[], date]):
        self._office_today = office_today
        self._lock = RLock()
        self._assets = {
            "REC-01": Asset("REC-01", "recorder"),
            "CAM-01": Asset("CAM-01", "camera"),
            "PROJ-01": Asset("PROJ-01", "projector"),
        }
        self._camera_training = {"EMP-01": True, "EMP-02": False}
        seed_request = ConfirmationRequest(
            operation_id="OP-SEED-01",
            asset_id="REC-01",
            start=date(2026, 11, 20),
            end=date(2026, 11, 21),
        )
        seed = Confirmation("CONF-SEED-01", "EMP-02", seed_request)
        self._confirmations = (seed,)
        self._operations = {("EMP-02", seed_request.operation_id): seed}
        self._next_reference = 1

    def catalogue(self, employee_id: str) -> tuple[Asset, ...]:
        with self._lock:
            self._require_employee(employee_id)
            return tuple(self._assets.values())

    def own_confirmations(self, employee_id: str) -> tuple[Confirmation, ...]:
        with self._lock:
            self._require_employee(employee_id)
            return tuple(
                confirmation
                for confirmation in self._confirmations
                if confirmation.employee_id == employee_id
            )

    def confirmation(self, employee_id: str, reference: str) -> Confirmation:
        with self._lock:
            self._require_employee(employee_id)
            for confirmation in self._confirmations:
                if (
                    confirmation.reference == reference
                    and confirmation.employee_id == employee_id
                ):
                    return confirmation

            # The same response for absent and inaccessible references avoids
            # confirming the existence of another employee's reservation.
            raise AccessDenied("Confirmation unavailable")

    def set_camera_training(self, employee_id: str, current: bool) -> None:
        """Trusted fixture control, not an employee-facing administration API."""
        with self._lock:
            self._require_employee(employee_id)
            if type(current) is not bool:
                raise InvalidRequest("Training state must be a boolean")

            self._camera_training[employee_id] = current

    def confirm(
        self,
        employee_id: str,
        request: ConfirmationRequest,
    ) -> Confirmation:
        with self._lock:
            self._require_employee(employee_id)
            self._validate_request(request)

            operation_key = (employee_id, request.operation_id)
            existing = self._operations.get(operation_key)
            if existing is not None:
                if existing.request != request:
                    raise ReservationConflict("Operation payload changed")

                # Recover the accepted result before checking today's rules.
                return existing

            today = self._office_today()
            if type(today) is not date:
                raise InvalidRequest("Office today must be a calendar date")

            if request.start < today or request.end < request.start:
                raise InvalidRequest("Invalid reservation dates")

            asset = self._assets[request.asset_id]
            duration = (request.end - request.start).days + 1
            self._validate_asset_rules(asset, employee_id, duration)

            for confirmation in self._confirmations:
                reserved = confirmation.request
                same_asset = reserved.asset_id == request.asset_id
                overlaps = (
                    request.start <= reserved.end
                    and reserved.start <= request.end
                )
                if same_asset and overlaps:
                    raise ReservationConflict("Asset unavailable for those dates")

            result = Confirmation(
                reference=f"CONF-{self._next_reference:04d}",
                employee_id=employee_id,
                request=request,
            )

            # Prepare both replacement collections before publishing either.
            # All readers/writers use this lock, including eligibility updates.
            confirmations = (*self._confirmations, result)
            operations = {**self._operations, operation_key: result}
            self._confirmations = confirmations
            self._operations = operations
            self._next_reference += 1
            return result

    def _require_employee(self, employee_id: str) -> None:
        if type(employee_id) is not str or employee_id not in self._camera_training:
            raise AccessDenied("Employee unavailable")

    def _validate_request(self, request: ConfirmationRequest) -> None:
        if type(request) is not ConfirmationRequest:
            raise InvalidRequest("Expected a confirmation request")

        for identifier in (request.operation_id, request.asset_id):
            if type(identifier) is not str or not identifier.strip():
                raise InvalidRequest("Identifiers must be nonblank strings")

        if request.asset_id not in self._assets:
            raise InvalidRequest("Unknown asset")

        if type(request.start) is not date or type(request.end) is not date:
            raise InvalidRequest("Dates must be calendar date values")

    def _validate_asset_rules(
        self,
        asset: Asset,
        employee_id: str,
        duration: int,
    ) -> None:
        policy = ASSET_POLICIES.get(asset.kind)
        if policy is None:
            raise InvalidRequest("Unknown asset kind")

        policy.validate(
            duration=duration,
            camera_training_current=self._camera_training[employee_id],
        )
