from datetime import datetime
from unittest.mock import Mock

# Save a couple of test days
wednesday = datetime(year=2025, month=1, day=1)
sunday = datetime(year=2025, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

# Mock .today() to return Wednesday
datetime.today.return_value = wednesday
# Test Wednesday is a weekday
assert is_weekday()

# Mock .today() to return Sunday
datetime.today.return_value = sunday
# Test Sunday is not a weekday
assert not is_weekday()