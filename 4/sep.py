#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print('-' * len(Belgium))
print(Belgium.replace(",", ":"))
split = Belgium.split(",")
print(int(split[1]) + int(split[3]))
print('-' * len(Belgium))
