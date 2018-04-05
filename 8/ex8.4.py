import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "country.txt"
abs_file_path = os.path.join(script_dir, rel_path)


def clean_line(string):
    string = string.rstrip()
    string = re.sub(r"'", "''", string)
    lrow = []
    for field in string.split(","):
        lrow.append("'"+field+"'")
    return ",".join(lrow)

for row in open(abs_file_path):
    print(clean_line(row))
