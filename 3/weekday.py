# Python 3 version

# Code for reading in the date */
date = input("Please enter date (DD/MM/YYYY): ")
d, m, y = date.split('/')
d = int(d)
m = int(m)
y = int(y)

if (y % 400) == 0:
    LEAP = True
elif (y % 100) == 0:
    LEAP = False
elif (y % 4) == 0:
    LEAP = True
else:
    LEAP = False

if LEAP and (m in (1, 2)):
    d -= 2
if not(LEAP) and (m in (1, 2)):
    d -= 1
if m in (1, 2):
    m += 12

z = 1 + d + (m * 2) + (3 * (m + 1) // 5) + y + y//4 - y//100 + y//400

z %= 7

days = ["Sun", "Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur"]

print(days[z]+'day')
