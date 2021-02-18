from django.test import TestCase
from .views import is_public_holiday, get_business_seconds
import datetime


class BusinessSeconds(TestCase):

    def test_is_public_holiday(self):
        """Tests that a given date is a public holiday"""
        self.assertEqual(is_public_holiday(2021-1-1), True)

    def test_get_business_seconds(self):
        """Tests the difference in seconds between two given dates """
        a = datetime.datetime(2021, 2, 15, 10, 0, 0)
        b = datetime.datetime(2021, 2, 26,  16, 0, 0)
        self.assertEqual(get_business_seconds(a, b), 313200)
