import math

day = 1  # 0 = sunday, 1 = monday, 2 = tuesday, ..., 6 = saturday
month = 1
year = 1900

def is_leap_year(n):
    """
    Returns True if n is a leap year (multiple of 4, not multiple of 100 unless multiple of 400) and False otherwise
    """
    if n % 4 == 0:
        if n % 400 == 0:
            return True
        elif n % 100 == 0:
            return False
        else:
            return True
    else:
        return False

class Date:
    """
    Defines a Date class with methods to keep track of day of week as we go from month to month
    The day_of_week variable tracks the day of the week for the first day of the month
    It is given in the problem that Jan 1, 1900 is a Monday
    """
    def __init__(self):
        self.year = 1900
        self.month = 1
        self.day_of_week = 1  # 0 = sunday, 1 = monday, ..., 6 = saturday

    def advance_year(self):
        self.day_of_week = (self.day_of_week + (366 if is_leap_year(self.year) else 365)) % 7
        self.year += 1

    def advance_month(self):
        # first deal with day of day of week
        if month == 2:
            self.day_of_week = (self.day_of_week + (29 if is_leap_year(self.year) else 28)) % 7
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            self.day_of_week = (self.day_of_week + 31) % 7
        else:
            self.day_of_week = (self.day_of_week + 30) % 7

        # month and year
        if month == 12:
            self.month == 1
            self.year += 1
        else:
            self.month += 1


def count_first_day_sundays(start_year, start_month, end_year, end_month):
    """
    Counts the number of Sundays that fall on the first day of a Month from start_month, start_year to end_month, end_year
    Both ends are inclusive
    """
    d = Date()
    count = 0
    while d.year < start_year:
        d.advance_year()
    while d.month < start_month:
        d.advance_month()
    while d.year < end_year or (d.year == end_year and d.month < end_month):
        if d.day_of_week == 0:
            count += 1
        d.advance_month()
    return count

print(count_first_day_sundays(1901, 1, 2000, 12))
