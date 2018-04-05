import decimal


def frange(start, stop, step=0.25):
    curr = start
    if step != 0:
        while curr <= stop:
            yield curr
            curr += step


vals = [(1.1, 3), (1, 3, 0.33), (1, 3, 1), (3, 1), (1, 3, 0), (-1, -0.5, 0.1)]

for val in vals:
    print(val)
    print(list(frange(*val)))

# for num in frange(3.142, 12):
#     print(f"{num:05.2f}")


# 2 allow single var


def frange(start, stop=None, step=0.25):
    if stop is None:
        stop = start
        start = 0.0
    curr = start
    if step != 0:
        while curr <= stop:
            yield curr
            curr += step

one = list(frange(0, 3.5, 0.25))
two = list(frange(3.5))
if one == two:
    print("Worked")
else:
    print("Computer says no")


# Part 3 use the decimal function

def frange(start, stop=None, step=0.25):
    start = decimal.Decimal(str(start))
    step = decimal.Decimal(str(step))
    if stop is None:
        stop = start
        start = decimal.Decimal(str(0.0))
    else:
        stop = decimal.Decimal(str(stop))
    curr = start
    if step != 0:
        while curr <= stop:
            yield float(curr)
            curr += step

for val in vals:
    print(val)
    print(list(frange(*val)))
