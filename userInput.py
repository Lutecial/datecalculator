#!./my_env/bin/python

from datediff import *

# prompt and accept user input for first and second date entry with some data validation
while True:
    counter = 0
    if counter == 0:
        print("Please enter first date:")
        entry = input().split("/")
        try:
            day = int(entry[0])
            month = int(entry[1])
            year = int(entry[2])
            firstdate = Date(day, month, year)
            counter += 1
        except:
            print("Invalid entry, the correct format is dd/mm/yyyy")
            continue
        if month != 2:
            if day > Days_in_Month[month - 1]:
                print("Please check the date on the month and try enter the correct date.")
                continue
        elif month == 2:
            if not isLeapYear(year):
                if day > 28:
                    print("Cannot accept days bigger than 28 if not leap year.")
                    continue
            if day > 29:
                print("There are maximum of 29 days in Feburary")
                continue
        if month > 12 or 1900 > year > 2999:
            print("Invalid date entry, the date should between 01/01/1900 and 31/12/2999")
            continue
    if counter == 1:
        print("Please enter second date:")
        entry = input().split("/")
        try:
            day = int(entry[0])
            month = int(entry[1])
            year = int(entry[2])
            seconddate = Date(day, month, year)
        except:
            print("Invalid entry, the correct format is dd/mm/yyyy")
            continue
        if month != 2:
            if day > Days_in_Month[month - 1]:
                print("Please check the date on the month and try enter the correct date.")
                continue
        elif month == 2:
            if not isLeapYear(year):
                if day > 28:
                    print("Cannot accept days bigger than 28 if not leap year.")
                    continue
            if day > 29:
                print("There are maximum of 29 days in Feburary")
                continue
        if month > 12 or 1900 > year > 2999:
            print("invalid date entry, the date should between 01/01/1900 and 31/12/2999")
            continue
        
        break

print(diffCalculation(firstdate, seconddate), "days")