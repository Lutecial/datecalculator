#!./my_env/bin/python

from datediff import Date, diffCalculation

# test unit set 1, should return "19"
date1 = Date(2, 6, 1983)
date2 = Date(22, 6, 1983)
if diffCalculation(date1, date2) == 19:
    print("Pass")
else:
    print("error")
# print(diffCalculation(date1, date2), "days")

# test unit set 2, should return "173"
date1 = Date(4, 7, 1984)
date2 = Date(25, 12, 1984)
if diffCalculation(date1, date2) == 173:
    print("Pass")
else:
    print("error")
# print(diffCalculation(date1, date2), "days")

# test unit set 3, should return "2036"
date1 = Date(1, 3, 1989)
date2 = Date(3, 8, 1983)
if diffCalculation(date1, date2) == 2036:
    print("Pass")
else:
    print("error")
# print(diffCalculation(date1, date2), "days")

# test unit set 4, same day test, shoud return "0"
date1 = Date(1, 1, 2001)
date2 = Date(1, 1, 2001)
if diffCalculation(date1, date2) == 0:
    print("Pass")
else:
    print("error")
# print(diffCalculation(date1, date2), "days")
