import unittest
from datetime import datetime, date
from birth import Discount

class DiscountTest(unittest.TestCase):
    def setUp(self):
        birth_date = date(datetime.now().year, 5, 31)
        registration_date = date(2022, 1, 15)
        self.discount = Discount("mohammad goodarzi", birth_date, registration_date)

    def test_birthday_discount(self):
        expected_discount = 0.5

        discount_rate = self.discount.apply_discount()

        self.assertEqual(discount_rate, expected_discount)

if __name__ == '__main__':
    unittest.main()
