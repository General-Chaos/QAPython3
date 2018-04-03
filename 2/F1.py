fuelperlap = 2.25
laps = 45
quallaptime = 80.45

minfuel = fuelperlap * laps * 1.5
print(minfuel)

firstlaptime = quallaptime + (((minfuel - 5)/10)*0.35)
print(firstlaptime)