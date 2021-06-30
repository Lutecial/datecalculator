# Python3 program to find number of days
# between two given dates
from datetime import date


def numOfDays(date1, date2):
    return abs((date2-date1).days) - 1


# Driver program
date1 = date(1989, 3, 1)
date2 = date(1983, 8, 3)
print(numOfDays(date1, date2), "days")
