#!./my_env/bin/python

Days_in_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def isBisextile(self):
        return True if self.year%4 == 0 else False

fulldate = Date(1983,8,3)

days = int(input("Enter number of days: \n"))

while days >= 0: 
    if fulldate.isBisextile():
        Days_in_Month[1] = 29
    else:
        Days_in_Month[1] = 28

    fulldate.date += 1

    if fulldate.date > int(Days_in_Month[fulldate.month-1]):
        fulldate.month += 1
        if fulldate.month > 12:
            fulldate.year += 1
            fulldate.month = 1
        fulldate.date = 1
    days -= 1

print("{}/{}/{}".format(fulldate.date,fulldate.month,fulldate.year))