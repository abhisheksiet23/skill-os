"""ER-1 behavior checks; supply ER1_IMPLEMENTATION to test a frozen variant."""

import importlib.util
import os
from pathlib import Path
import sys
from concurrent.futures import ThreadPoolExecutor, wait
from dataclasses import replace
from datetime import date, datetime
from threading import Barrier, Event
import unittest
from unittest.mock import patch


implementation = Path(
    os.environ.get(
        "ER1_IMPLEMENTATION",
        str(Path(__file__).with_name("reservations.py")),
    )
)
spec = importlib.util.spec_from_file_location("er1_implementation", implementation)
domain = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = domain
spec.loader.exec_module(domain)


class ReservationContract(unittest.TestCase):
    def setUp(self):
        self.today = date(2026, 11, 18)
        self.service = domain.Reservations(lambda: self.today)

    def request(self, asset="REC-01", start=22, end=23, operation="OP-01"):
        return domain.ConfirmationRequest(
            operation_id=operation,
            asset_id=asset,
            start=date(2026, 11, start),
            end=date(2026, 11, end),
        )

    def snapshot(self):
        return (
            self.service.own_confirmations("EMP-01"),
            self.service.own_confirmations("EMP-02"),
        )

    def reject_unchanged(self, error, employee, request):
        before = self.snapshot()
        with self.assertRaises(error):
            self.service.confirm(employee, request)
        self.assertEqual(before, self.snapshot())

    def test_three_asset_consumers_accept_their_inclusive_limits(self):
        for asset, start, end in (
            ("REC-01", 22, 28),
            ("CAM-01", 18, 20),
            ("PROJ-01", 18, 20),
        ):
            with self.subTest(asset=asset):
                request = self.request(asset, start, end, operation=asset)
                confirmed = self.service.confirm("EMP-01", request)
                self.assertEqual(request, confirmed.request)
                self.assertEqual("EMP-01", confirmed.employee_id)
                self.assertTrue(confirmed.reference)

        self.assertEqual(3, len(self.service.own_confirmations("EMP-01")))

    def test_each_consumer_rejects_one_day_over_its_limit(self):
        for asset, start, end in (
            ("REC-01", 22, 29),
            ("CAM-01", 18, 21),
            ("PROJ-01", 18, 21),
        ):
            with self.subTest(asset=asset):
                self.reject_unchanged(
                    domain.InvalidRequest,
                    "EMP-01",
                    self.request(asset, start, end),
                )

    def test_same_day_is_one_day(self):
        result = self.service.confirm("EMP-01", self.request(start=18, end=18))
        self.assertEqual(date(2026, 11, 18), result.request.end)

    def test_dates_before_today_and_reversed_dates_do_not_mutate(self):
        for start, end in ((17, 18), (23, 22)):
            self.reject_unchanged(
                domain.InvalidRequest,
                "EMP-01",
                self.request(start=start, end=end),
            )

    def test_training_is_rechecked_after_catalogue_display(self):
        self.assertEqual(3, len(self.service.catalogue("EMP-01")))
        self.service.set_camera_training("EMP-01", False)
        self.reject_unchanged(
            domain.AccessDenied,
            "EMP-01",
            self.request("CAM-01", 18, 19),
        )

    def test_untrained_employee_can_reserve_other_asset_types(self):
        for asset, start, end in (("REC-01", 22, 23), ("PROJ-01", 18, 19)):
            result = self.service.confirm(
                "EMP-02",
                self.request(asset, start, end, operation=asset),
            )
            self.assertEqual("EMP-02", result.employee_id)

        self.reject_unchanged(
            domain.AccessDenied,
            "EMP-02",
            self.request("CAM-01", 18, 19),
        )

    def test_overlap_includes_both_endpoints_and_containment(self):
        for start, end in ((19, 20), (21, 22), (20, 21), (19, 22), (20, 20)):
            self.reject_unchanged(
                domain.ReservationConflict,
                "EMP-01",
                self.request(start=start, end=end),
            )

    def test_adjacent_nonoverlap_and_different_assets_are_allowed(self):
        for asset, start, end in (
            ("REC-01", 18, 19),
            ("REC-01", 22, 23),
            ("PROJ-01", 20, 21),
        ):
            self.service.confirm(
                "EMP-01",
                self.request(asset, start, end, operation=f"{asset}-{start}"),
            )

        self.assertEqual(3, len(self.service.own_confirmations("EMP-01")))

    def test_lost_response_retry_returns_existing_effect(self):
        request = self.request()

        def lose_response():
            self.service.confirm("EMP-01", request)
            raise TimeoutError("Synthetic response loss after service acceptance")

        with self.assertRaises(TimeoutError):
            lose_response()

        committed = self.service.own_confirmations("EMP-01")[0]
        recovered = self.service.confirm("EMP-01", request)
        self.assertEqual(committed, recovered)
        self.assertEqual(1, len(self.service.own_confirmations("EMP-01")))

    def test_replay_does_not_recheck_training_or_today(self):
        request = self.request("CAM-01", 18, 20)
        original = self.service.confirm("EMP-01", request)
        self.service.set_camera_training("EMP-01", False)
        self.today = date(2026, 12, 1)
        self.assertEqual(original, self.service.confirm("EMP-01", request))

    def test_er_limit_preserves_confirmation_accepted_under_two_day_policy(self):
        legacy_policies = dict(domain.ASSET_POLICIES)
        legacy_policies["projector"] = replace(
            legacy_policies["projector"],
            maximum_days=2,
        )
        legacy_request = self.request("PROJ-01", 18, 19, operation="LEGACY")

        # Establish the existing record under the old rule in this same service.
        # Restoring the module policy simulates an in-process rule change only.
        with patch.object(domain, "ASSET_POLICIES", legacy_policies):
            legacy = self.service.confirm("EMP-01", legacy_request)

        self.assertEqual((legacy,), self.service.own_confirmations("EMP-01"))
        self.today = date(2026, 12, 1)
        replay = self.service.confirm("EMP-01", legacy_request)
        self.assertIs(legacy, replay)
        self.assertEqual((legacy,), self.service.own_confirmations("EMP-01"))

        self.today = date(2026, 11, 18)
        new_request = self.request("PROJ-01", 22, 24, operation="NEW-LIMIT")
        new = self.service.confirm("EMP-01", new_request)
        self.assertEqual(new_request, new.request)
        self.assertEqual((legacy, new), self.service.own_confirmations("EMP-01"))
        self.assertIs(legacy, self.service.confirm("EMP-01", legacy_request))

    def test_operation_payload_changes_conflict_without_mutation(self):
        self.service.confirm("EMP-01", self.request())
        changes = (
            self.request(asset="PROJ-01"),
            self.request(start=23),
            self.request(end=24),
        )
        for changed in changes:
            self.reject_unchanged(domain.ReservationConflict, "EMP-01", changed)

    def test_operation_identifiers_are_exact_not_trimmed(self):
        first = self.service.confirm("EMP-01", self.request(operation=" OP "))
        second = self.service.confirm(
            "EMP-01",
            self.request(start=24, end=25, operation="OP"),
        )
        self.assertNotEqual(first.reference, second.reference)

    def test_operation_identity_is_scoped_to_employee(self):
        first = self.service.confirm("EMP-01", self.request())
        self.reject_unchanged(domain.ReservationConflict, "EMP-02", self.request())
        second = self.service.confirm(
            "EMP-02",
            self.request(start=24, end=25),
        )
        self.assertNotEqual(first.reference, second.reference)
        self.assertEqual("EMP-02", second.employee_id)

    def test_own_list_and_direct_read_do_not_disclose_other_employee(self):
        self.assertEqual((), self.service.own_confirmations("EMP-01"))
        seed = self.service.own_confirmations("EMP-02")[0]
        self.assertEqual("CONF-SEED-01", seed.reference)
        messages = []
        for reference in (seed.reference, "MISSING"):
            with self.assertRaises(domain.AccessDenied) as caught:
                self.service.confirmation("EMP-01", reference)
            messages.append(str(caught.exception))

        self.assertEqual(messages[0], messages[1])
        self.assertEqual(seed, self.service.confirmation("EMP-02", seed.reference))

    def test_unknown_and_malformed_identity_is_denied(self):
        for employee in (None, True, [], "", " EMP-01 ", "MISSING"):
            with self.subTest(employee=employee):
                self.reject_unchanged(domain.AccessDenied, employee, self.request())
                with self.assertRaises(domain.AccessDenied):
                    self.service.own_confirmations(employee)
                with self.assertRaises(domain.AccessDenied):
                    self.service.catalogue(employee)

    def test_malformed_identifiers_are_rejected_without_mutation(self):
        for invalid in (None, True, 2, [], "", "  "):
            for field in ("operation_id", "asset_id"):
                values = vars(self.request()) | {field: invalid}
                with self.subTest(field=field, invalid=invalid):
                    self.reject_unchanged(
                        domain.InvalidRequest,
                        "EMP-01",
                        domain.ConfirmationRequest(**values),
                    )

    def test_unknown_or_normalized_asset_is_not_silently_accepted(self):
        for asset in ("MISSING", "rec-01", " REC-01 "):
            self.reject_unchanged(
                domain.InvalidRequest,
                "EMP-01",
                self.request(asset=asset),
            )

    def test_dates_require_date_values_not_strings_datetimes_or_booleans(self):
        for invalid in (None, True, "2026-11-22", datetime(2026, 11, 22)):
            for field in ("start", "end"):
                values = vars(self.request()) | {field: invalid}
                self.reject_unchanged(
                    domain.InvalidRequest,
                    "EMP-01",
                    domain.ConfirmationRequest(**values),
                )

    def test_request_shape_is_explicit(self):
        for invalid in (None, {}, True):
            self.reject_unchanged(domain.InvalidRequest, "EMP-01", invalid)

    def test_rejection_does_not_consume_operation_identity(self):
        self.reject_unchanged(
            domain.ReservationConflict,
            "EMP-01",
            self.request(start=20, end=21),
        )
        confirmed = self.service.confirm("EMP-01", self.request())
        self.assertEqual("CONF-0001", confirmed.reference)

    def test_returned_confirmations_cannot_mutate_service_state(self):
        from dataclasses import FrozenInstanceError

        confirmed = self.service.confirm("EMP-01", self.request())
        with self.assertRaises(FrozenInstanceError):
            confirmed.employee_id = "EMP-02"
        with self.assertRaises(FrozenInstanceError):
            confirmed.request.asset_id = "CAM-01"
        self.assertEqual(confirmed, self.service.own_confirmations("EMP-01")[0])

    def race(self, employees, requests):
        barrier = Barrier(len(employees))

        def attempt(employee, request):
            barrier.wait(timeout=5)
            try:
                return self.service.confirm(employee, request)
            except domain.ReservationConflict:
                return None

        with ThreadPoolExecutor(max_workers=len(employees)) as executor:
            futures = [
                executor.submit(attempt, employee, request)
                for employee, request in zip(employees, requests)
            ]
            return [future.result(timeout=10) for future in futures]

    def test_concurrent_conflicting_confirmations_have_one_winner(self):
        results = self.race(
            ["EMP-01", "EMP-02"],
            [self.request(operation="A"), self.request(operation="B")],
        )
        winners = [result for result in results if result is not None]
        self.assertEqual(1, len(winners))
        self.assertEqual(2, sum(map(len, self.snapshot())))
        winner = winners[0]
        self.assertEqual(
            winner,
            self.service.confirm(winner.employee_id, winner.request),
        )

    def test_concurrent_identical_replays_create_one_effect(self):
        request = self.request()
        results = self.race(["EMP-01"] * 8, [request] * 8)
        self.assertTrue(all(result == results[0] for result in results))
        self.assertEqual(1, len(self.service.own_confirmations("EMP-01")))

    def test_competing_writer_cannot_commit_during_paused_overlap_scan(self):
        scan_paused = Event()
        release_scan = Event()
        second_started = Event()

        class PauseFirstScan(tuple):
            def __iter__(self):
                yield from super().__iter__()
                if not scan_paused.is_set():
                    # Controlled interruption after examining current bookings,
                    # immediately before the first writer can publish a result.
                    scan_paused.set()
                    if not release_scan.wait(timeout=5):
                        raise TimeoutError("Overlap-scan test was not released")

        self.service._confirmations = PauseFirstScan(self.service._confirmations)

        def attempt(employee, operation):
            if employee == "EMP-02":
                second_started.set()
            try:
                return self.service.confirm(
                    employee,
                    self.request(operation=operation),
                )
            except domain.ReservationConflict:
                return None

        with ThreadPoolExecutor(max_workers=2) as executor:
            first = executor.submit(attempt, "EMP-01", "FIRST")
            try:
                self.assertTrue(scan_paused.wait(timeout=5))
                second = executor.submit(attempt, "EMP-02", "SECOND")
                self.assertTrue(second_started.wait(timeout=5))
                completed, _ = wait([second], timeout=0.05)
            finally:
                release_scan.set()

            results = [first.result(timeout=5), second.result(timeout=5)]

        self.assertEqual(set(), completed)
        self.assertEqual(1, sum(result is not None for result in results))
        self.assertEqual(2, sum(map(len, self.snapshot())))

    def test_concurrent_changed_payload_under_same_operation_has_one_effect(self):
        results = self.race(
            ["EMP-01", "EMP-01"],
            [self.request(), self.request(start=24, end=25)],
        )
        self.assertEqual(1, sum(result is not None for result in results))
        self.assertEqual(1, len(self.service.own_confirmations("EMP-01")))


if __name__ == "__main__":
    unittest.main()
