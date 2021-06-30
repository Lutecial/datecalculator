#!./my_env/bin/python

from datediff import Date, diffCalculation

# test unit
date1 = Date(2, 6, 1983)
date2 = Date(22, 6, 1983)
print(diffCalculation(date1, date2), "days")

