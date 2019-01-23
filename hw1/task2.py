import math
import pylab
import numpy as np
import functools as ft
import scipy.stats as st
import matplotlib.pyplot as plt

eps = 10 ** (-6)

def wa(z):
    res = 0
    for k in range(1, 1000010):
        res += 1 / (k ** 2 - k - z)
    return res

def wb(z):
    res = 1
    for k in range(1, 1500):
        res += (2 * k + z) / ((k ** 2 - k - z) * (k ** 2 + k))
    return res

def diff_wa_wb(z):
    return wa(z) - wb(z)

shards = 100

xlist = [i * (2 / shards) for i in range(1, shards)]
ylist_wa = [wa(x) for x in xlist]
ylist_wb = [wb(x) for x in xlist]
ylist_diff = [diff_wa_wb(x) for x in xlist]

pylab.clf()
pylab.plot (xlist, ylist_wa)
pylab.savefig("wa-chart.png")

pylab.clf()
pylab.plot (xlist, ylist_wb)
pylab.savefig("wb-chart.png")

pylab.clf()
pylab.plot (xlist, ylist_diff)
pylab.axhline(2 * eps, color='red')
pylab.savefig("diff-chart-with-epsilon.png")

pylab.clf()
pylab.plot (xlist, ylist_diff)
pylab.savefig("diff-chart.png")
