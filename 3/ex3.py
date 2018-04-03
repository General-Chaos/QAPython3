import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# Use the glob.glob() function to obtain the list of filenames
files = glob.glob(pattern)
for file in files:
    size = os.path.getsize(file)
    if size > 0:
        print(os.path.basename(file))
