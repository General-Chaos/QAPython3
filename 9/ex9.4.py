import getprocs


def igetprocs():
    proc = getprocs.getfirstproc()
    while proc:
        yield proc
        proc = getprocs.getnextproc()

procdict = {pid: [ppid, name] for pid, ppid, name in igetprocs()}
print(procdict)
