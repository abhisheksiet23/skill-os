import unittest

from quotas import remaining_quota


class RemainingQuotaTests(unittest.TestCase):
    def test_subtracts_used_quota(self):
        self.assertEqual(remaining_quota(10, 4), 6)

    def test_rejects_negative_values(self):
        with self.assertRaises(ValueError):
            remaining_quota(-1, 0)


if __name__ == "__main__":
    unittest.main()
