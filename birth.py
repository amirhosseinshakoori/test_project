from datetime import date
import logging

class Discount:
    def __init__(self, username, birth_date, registration_date):
        self.username = username
        self.birth_date = birth_date
        self.registration_date = registration_date

    def apply_discount(self):
        """
        get birthday and get today datetime and calculate if you get fifty precent for discount
        """
        today = date.today()
        if today.month == self.birth_date.month and today.day == self.birth_date.day:
            discount_rate = 0.5  # 50% discount on the ticket price
            logging.debug(f"{self.username} is eligible for a birthday discount")
            return discount_rate
        else:
            months_as_member = (today.year - self.registration_date.year) * 12 + (
                    today.month - self.registration_date.month)
            discount_rate = 0.05  # 5% discount for every month of membership
            discount_rate = min(months_as_member * discount_rate, 0.3)  # maximum discount rate of 30%
            return discount_rate



