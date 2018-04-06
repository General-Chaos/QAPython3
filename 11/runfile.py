import sys
import os
from myfile import MyFile

script_dir = os.path.dirname(__file__)
rel_path = "country.txt"
abs_file_path = os.path.join(script_dir, rel_path)

filea = MyFile(abs_file_path)
print(filea.get_fname(), "is", len(filea), "bytes")
