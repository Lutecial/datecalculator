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

def countLeapYear(x):
    yrs = x.year
    if (x.month <= 2):
        yrs -= 1
    return int(yrs / 4) - int(yrs / 100) + int(yrs / 400)

def diffCalculation(date1, date2):
    year1 = date1.year
    year2 = date2.year
    yearCount = int()
    p1 = date1.year * 365 + date1.day
    for i in range (0, date1.month - 1):
        p1 += Days_in_Month[i]
    p1 += countLeapYear(date1)

    p2 = date2.year * 365 + date2.day
    for i in range (0, date2.month - 1):
        p2 += Days_in_Month[i]
    p2 += countLeapYear(date2)

    minPosition = min(p1,p2)
    maxPosition = max(p1,p2)

    return maxPosition - minPosition - 1

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
    if day1 > Days_in_Month[month1 -1]:
        print("please check the date on the month and try enter the correct date.")
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
    if day2 > Days_in_Month[month2 -1]:
        print("please check the date on the month and try enter the correct date.")
        continue
    break

firstdate = Date(day1, month1, year1)
seconddate = Date(day2, month2, year2)
print(diffCalculation(firstdate, seconddate), "days")
