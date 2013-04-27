#!/usr/bin/python

# CMSC 12300 - Computer Science with Applications 3
# Borja Sotomayor, 2013

# Generate a graph based on the data produced by
# the performance-test script

import sys
import re
import pylab

fname = sys.argv[1]

f = open(fname)

f.readline() # skip header

solvers = {}

for line in f:
    solver, lineq, time = line.split(",")
    
    lineq = int(re.sub("[^0-9]", "", lineq))
    time = float(time)

    solvers.setdefault(solver, {}).setdefault(lineq, []).append(time)

for solver in solvers:
    for lineq in solvers[solver]:
        times = solvers[solver][lineq]
        avg = sum(times) / len(times)
        solvers[solver][lineq] = avg

pylab.figure()
#pylab.yscale("log")

solvernames = sorted(solvers.keys())
for solver in solvernames:
    items = sorted(solvers[solver].items())
    leqs = [x[0] for x in items]
    times = [x[1] for x in items]
    pylab.plot(leqs, times)
    
pylab.title("Running time of several Jacobi method implementations")
pylab.ylabel("Time (seconds)")
pylab.xlabel("Number of variables")
pylab.legend(solvernames)

pylab.show()







