#User inputs year to be checked!
year = input("Enter the year : ")

#System checks the year given!
def leap_year():
    check1 = int(year) % 4
    check2 = int(year) % 100
    check3 = int(year) % 400
    if check1 == 0 and check2 != 0:
        return True
    elif check2 == 0 and check3 == 0:
        return True
    else:
        return False

#Prints out leap year or not!
if leap_year():
    print("This year is a leap year!")
else:
    print("This year is not a leap year!")