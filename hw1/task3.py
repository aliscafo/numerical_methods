import math
import pylab
import numpy as np
import functools as ft
import scipy.stats as st
import matplotlib.pyplot as plt

N1 = 10 ** 4
N2 = 10 ** 2


def ak(z, k):
    return 1 / (2 * k - 1) * (z ** k)

def aitken(z, n):
    a = z 
    b = a + ak(z, 2) 
    c = b + ak(z, 3)
    ds = c - (c - b) ** 2 / (c - 2 * b + a) 
    for i in range(4, n): 
        a, b = b, c
        c += ak(z, i)
        if (c - 2 * b + a) != 0: 
            ds = c - (c - b) ** 2 / (c - 2 * b + a)
    return ds

def conv_speed(x):
    z = np.exp(x * math.pi * 1j)
    return abs(aitken(z, N1) - aitken(z, N2))


file = open('result.txt', 'w')
file.write('for -0.9:' + '\n')
file.write(str(aitken(-0.9, N1)) + '\n\n')
file.write('for -1:' + '\n')
file.write(str(aitken(-1, N1)) + '\n\n')
file.write('for exp(3 * 1j * pi / 4):' + '\n')
file.write(str(aitken(np.exp(3 * 1j * math.pi / 4), N1)) + '\n\n')
file.write('for 1j:' + '\n')
file.write(str(aitken(1j, N1)) + '\n\n')
file.close()


shards = 50

# промежуток, где угол от -pi до 0-
xlist_left = [i * (1 / shards) for i in range(-shards, 0)]
ylist_left = [conv_speed(x) for x in xlist_left]

# промежуток, где угол от 0+ до pi
xlist_right = [i * (1 / shards) for i in range(1, shards + 1)]
ylist_right = [conv_speed(x) for x in xlist_right]

pylab.clf()
pylab.plot (xlist_left, ylist_left)
pylab.savefig("aitken_chart_left.png")

pylab.clf()
pylab.plot (xlist_right, ylist_right)
pylab.savefig("aitken_chart_right.png")