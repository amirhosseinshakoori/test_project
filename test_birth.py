import unittest
from datetime import date
from birth import Discount

class DiscountTest(unittest.TestCase):
    def test_birthday_discount(self):
        # Set up
        today = date.today()
        username = "JohnDoe"
        birth_date = date(today.year, today.month, today.day)  # Same birth date as today
        registration_date = date(2022, 1, 1)  # A specific registration date
        discount = Discount(username, birth_date, registration_date)

        # Apply discount
        result = discount.apply_discount()

        # Check if the discount rate is correct
        self.assertEqual(result, 0.5)

    def test_membership_discount(self):
        # Set up
        today = date.today()
        username = "JaneSmith"
        birth_date = date(2000, 5, 1)  # A specific birth date
        registration_date = date(today.year, today.month, today.day)  # Same registration date as today
        discount = Discount(username, birth_date, registration_date)

        # Apply discount
        result = discount.apply_discount()

        # Calculate the expected discount rate
        months_as_member = (today.year - registration_date.year) * 12 + (today.month - registration_date.month)
        expected_discount_rate = min(months_as_member * 0.05, 0.3)

        # Check if the discount rate is correct
        self.assertEqual(result, expected_discount_rate)

if __name__ == '__main__':
    unittest.main()