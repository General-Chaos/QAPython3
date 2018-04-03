import getpass
PIN = "1234"

supplied_pin = getpass.getpass("Enter your PIN:")
attempts = 3
if supplied_pin != PIN:
    for i in range(1, attempts):
        supplied_pin = getpass.getpass("Incorrect PIN you have "+str(attempts-i)+" remaining attemps:")
        if supplied_pin == PIN:
            print("Correct PIN Entered")
        if (attempts-i == 1):
            print("Incorrect PIN entered after "+str(attempts)+" attempts.")
else:
    print("Correct PIN entered.")
