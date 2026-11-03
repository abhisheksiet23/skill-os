import unittest

from receipt import amount_to_cents


class ReceiptTests(unittest.TestCase):
    def test_whole_amount(self):
        self.assertEqual(amount_to_cents("12"), 1200)

    def test_refund(self):
        self.assertEqual(amount_to_cents("-1.25"), -125)


if __name__ == "__main__":
    unittest.main()
