"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime


def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month < 12:
        given_date = datetime.date(year, month, 1)
        comparing_date = datetime.date(year, month + 1, 1)
        difference = (comparing_date - given_date).days
        return difference
    elif month == 12:
        given_date = datetime.date(year, month, 1)
        comparing_date = datetime.date(year + 1, month - 11, 1)
        difference = (comparing_date - given_date).days
        return difference



def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if (year < 1) or (year > 9999):
        return False
    elif ((month < 1) or (month > 12)):
        return False
    elif ((day < 1) or (day > 31)):
        return False
    elif (month == 2) and (day > 28):
        valid_day = (days_in_month(year, month))
        is_it_valid = (valid_day == day)
        return is_it_valid
    elif day == 31:
        correct_day = (days_in_month(year, month))
        is_valid = correct_day == day
        return is_valid

    else:
        return True



def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    is_date1_valid = is_valid_date(year1, month1, day1)
    is_date2_valid = is_valid_date(year2, month2, day2)

    if is_date1_valid is False:
        return 0
    elif is_date2_valid is False:
        return 0
    elif (datetime.date(year1, month1, day1)) > (datetime.date(year2, month2, day2)):
        return 0
    else:
        return ((datetime.date(year2, month2, day2)) - (datetime.date(year1, month1, day1))).days





def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    is_date_valid = (is_valid_date(year, month, day))

    if is_date_valid is False:
        return 0

    elif (datetime.date(year, month, day)) > datetime.date.today():
        return 0
    else:
        return ((datetime.date.today()) - (datetime.date(year, month, day))).days




