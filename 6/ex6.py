# Exercise 6, string formatting and regular expressions
import re
import os

script_dir = os.path.dirname(__file__)
rel_path = "postcodes.txt"
abs_file_path = os.path.join(script_dir, rel_path)
infile = open(abs_file_path, 'r')

valid_file_path = os.path.join(script_dir, 'validpc.txt')
valid = open(valid_file_path).read().splitlines()
validpc = dict()
for txt in valid:
    kv = txt.split(",")
    validpc[kv[0]] = kv[1]


# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0

for postcode in infile:
    # The variable 'postcode' contain the line read from the file

    # Ignore empty lines
    if postcode.isspace():
        continue

    # TODO (a): Remove newlines, tabs and spaces
    postcode = re.sub(r"\s", "", postcode)
    # TODO (a): Convert to uppercase
    postcode = postcode.upper()
    # TODO (a): Insert a space before the final digit and 2 letters
    postcode = re.sub(r"(\d\w\w)$", r" \1", postcode)
    # Print the reformatted postcode
    print(postcode)

    # TODO (b) Validate the postcode, returning a match object 'm'
    m = re.search(r"^[A-Z]{1,2}\d{1,2}[A-Z]? \d[A-Z]{2}$", postcode)

    if m:
        valid = valid + 1
        if (postcode.split(' '))[0] in validpc:
            country = validpc[(postcode.split(' '))[0]]
            print(f"Postcode: {postcode} is from {country}")
        else:
            print(f"Postcode: {postcode} not found!")
    else:
        invalid = invalid + 1


infile.close()

# TODO (b) Print the valid and invalid totals
print(f"Valid:{valid} Invalid:{invalid}")
