import unittest
from unittest.mock import patch
from datetime import datetime

def is_weekday():
    today = datetime.today()
    return (0 <= today.weekday() < 5)

sato = datetime(year=2025, month=11, day=15)
cov_date = datetime(year=2025, month=6, day=18)

class TestHoliday(unittest.TestCase):
    @patch('__main__.datetime')  # Patch datetime in the module where is_holiday is defined.
    def test_false(self, mock_datetime): # patch() uses this parameter(mock_datetime) to pass the mocked object into your test. From there, you can modify the mock or make assertions as necessary.
        mock_datetime.today.return_value = sato
        self.assertFalse(is_weekday())

    # You can also use patch as a context manager, not necessarily a decorator
    def test_true(self):
        with patch("__main__.datetime") as mock_datetime:
            mock_datetime.today.return_value = cov_date
            self.assertTrue(is_weekday())

if __name__ == "__main__":
    unittest.main()

