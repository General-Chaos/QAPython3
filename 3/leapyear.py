year = int(input('Please enter a year :'))

if (year % 400) == 0:
    LEAP = True
elif (year % 100) == 0:
    LEAP = False
elif (year % 4) == 0:
    LEAP = True
else:
    LEAP = False

print(LEAP)
