import sys

var = input("Please enter an integer:")

if not var.isdecimal():
    sys.exit("ERROR: Input is not an integer")
var = int(var)
while var >= 0:
    print(var)
    var -= 2
