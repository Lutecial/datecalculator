#!./my_env/bin/python

# define days for each month
Days_in_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = int()

# define date
class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    # define leap year
    def isBisextile(self):
        return True if self.year%4 == 0 else False

firstEntry = input("Enter first date: \n").split("/")

secondEntry = input("Enter second date: \n").split("/")

year1 = int(firstEntry[0])
year2 = int(secondEntry[0])

month1 = int(firstEntry[1])
month2 = int(secondEntry[1])

date1 = int(firstEntry[2])
date2 = int(secondEntry[2])

firstdate = Date(year1, month1, date1)

seconddate = Date(year2, month2, date2)

# year is different
def yeardiff():
    return True if year1 != year2 else False
# month is different
def monthdiff():
    return True if month1 != month2 else False
# date is different
def datediff():
    return True if date1 != date2 else False


    # while datediff():
    #     if date1 < date2:
    #         date1 += 1
    #     elif date1 > date2:
    #         date2 += 1
    #     days += 1


# for x in secondEntry:
#     dateEntry.append(x)

# print (dateEntry)

# yeardiff = abs(secondfulldate.year - firstfulldate.year)

# monthdiff = abs(secondfulldate.month - firstfulldate.month)

# datediff = abs(secondfulldate.date - firstfulldate.date)

# while firstfulldate.year !=

    # if secondfulldate.month - firstfulldate.month == 0:
    #     days = secondfulldate.date - firstfulldate.date - 1
    #     print("days are: {}".format(days))

# days = int(input("Enter number of days: \n"))

# while days >= 0:
#     if firstdate.isBisextile():
#         Days_in_Month[1] = 29
#     else:
#         Days_in_Month[1] = 28

#     firstdate.date += 1

#     if firstdate.date > int(Days_in_Month[firstdate.month-1]):
#         firstdate.month += 1
#         if firstdate.month > 12:
#             firstdate.year += 1
#             firstdate.month = 1
#         firstdate.date = 1
#     days -= 1

# print("{}/{}/{}".format(firstdate.date,firstdate.month,firstdate.year))