def myfunc(value, alist=[]):
    alist.append(value)
    print(alist)

myfunc(1)
myfunc(2)
myfunc(3)

# To fix we need to clear the list each time and assign it if it is empty


def myfunc(value, alist=None):
    if alist is None:
        alist = []
    alist.append(value)
    print(alist)

myfunc(1)
myfunc(2)
myfunc(3)
