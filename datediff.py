#!./my_env/bin/python

# define days for each month
Days_in_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# define a date


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

# define leap year rule:
# The year must be evenly divisible by 4
# If the year can also be evenly divided by 100, it is not a leap year
# unless...
# The year is also evenly divisible by 400. Then it is a leap year.


def isLeapYear(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def countLeapYear(x):
    yrs = x.year
    # if current month is smaller than 2 means this year donot need to be considered leap year or not at all
    if (x.month <= 2):
        yrs -= 1
    # return the total count of leap years between entry year and start year 00/00/0000
    return int(yrs / 4) - int(yrs / 100) + int(yrs / 400)

# calculate the difference between two date entry against start date 00/00/0000


def diffCalculation(date1, date2):
    # initialise p1(first date entry) and calculate it against start date 00/00/0000 without month data
    p1 = date1.year * 365 + date1.day

    # calculate total days in month position for p1 (entry position 1) adding it to exisiting p1 result without leap year consideration
    for i in range(0, date1.month - 1):
        p1 += Days_in_Month[i]

    # adding leapyears into final days count (each leap year means an extra day to add)
    p1 += countLeapYear(date1)

    # same process for p2 (second date entry)
    p2 = date2.year * 365 + date2.day

    for i in range(0, date2.month - 1):
        p2 += Days_in_Month[i]

    p2 += countLeapYear(date2)

    # compare two entries and decide and low position in time line and the high position in time line
    minPosition = min(p1, p2)
    maxPosition = max(p1, p2)

    # calculate the position difference (date difference) between two entries. minus 1 day for not counting two entry date.
    return maxPosition - minPosition - 1


# prompt and accept user input for first and second date entry with some data validation

def userInput():
    while True:
        print("Please enter first date:")
        entry = input().split("/")
        try:
            day1 = int(entry[0])
            month1 = int(entry[1])
            year1 = int(entry[2])
        except:
            print("error, please enter the right format")
            continue
        if month1 != 2:
            if day1 > Days_in_Month[month1 - 1]:
                print("please check the date on the month and try enter the correct date.")
                continue
        elif month1 == 2:
            if not isLeapYear(year1):
                if day1 > 28:
                    print("cannot accept days bigger than 28 if not leap year.")
                    continue
        break
    while True:
        print("Please enter second date:")
        entry = input().split("/")
        try:
            day2 = int(entry[0])
            month2 = int(entry[1])
            year2 = int(entry[2])
        except:
            print("error, please enter the right format")
            continue
        if month2 != 2:
            if day2 > Days_in_Month[month2 - 1]:
                print("please check the date on the month and try enter the correct date.")
                continue
        elif month2 == 2:
            if not isLeapYear(year2):
                if day2 > 28:
                    print("cannot accept days bigger than 28 if not leap year.")
                    continue
        break

    firstdate = Date(day1, month1, year1)
    seconddate = Date(day2, month2, year2)
    print(diffCalculation(firstdate, seconddate), "days")
