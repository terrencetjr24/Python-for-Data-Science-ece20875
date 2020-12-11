#!/usr/bin/python3
year=2020
# Your code should be below this line
#test code, not intended for submission
#testList = [800, 2020, 583, 1100, 1994, 2015, 3132]
#for year in testList:
    #print("The year is", year)
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            #leap year
            print(True)
        else :
            #not leap year
            print(False)
    else :
        #leap year
        print(True)
else :
    #not leap year
    print(False)
