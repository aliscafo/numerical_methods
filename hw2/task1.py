import math
import pylab
import numpy as np

shards = 800

def lagrange(xs, fs, x):
    n = len(xs)
    res = 0
        
    for k in range (0, n):
        prod = 1
        for i in range(0, n):
            if (i == k):
                continue
            prod *= (x - xs[i]) / (xs[k] - xs[i])
        
        res += fs[k] * prod
    
    return res


def fs(x):
    return x * math.sin(2 * x)

def fm(x):
    return abs(x - 1)

def gen_uni_points(a, b, n):
    points = [a + i * (b - a) / (n - 1) for i in range(0, n)]
    return points
  
def gen_cheb_points(a, b, n):
    cheb_points = [math.cos(math.pi / 2 * (2 * k - 1) / n) for k in range(1, n + 1)]
    points = [0.5 * (a + b) + 0.5 * (b - a) * x for x in cheb_points]
    
    return points

def intrplt_pol_for_func_uni(func, a, b, n, x):
    nodes = gen_uni_points(a, b, n + 1)
    values = [func(x) for x in nodes]
    
    return lagrange(nodes, values, x)

def intrplt_pol_for_func_cheb(func, a, b, n, x):
    nodes = gen_cheb_points(a, b, n + 1)
    values = [func(x) for x in nodes]
    
    return lagrange(nodes, values, x)

def draw_diff_chart(func, a, b, n, file):
    xlist = gen_uni_points(a, b, shards)
    ylist_func = [func(x) for x in xlist]
    ylist_interp = [intrplt_pol_for_func_uni(func, a, b, n, x) for x in xlist]
    y_list_diff = [abs(ylist_func[i] - ylist_interp[i]) for i in range(0, shards)]
    
    ymax = max(y_list_diff)
    file.write(str(ymax) + '\n')
    print(ymax)
    
    pylab.clf()
    pylab.plot(xlist, y_list_diff, 'g')
    pylab.savefig("f1n" + str(n) + ".png")

def find_max(func, a, b, n):
    xlist = gen_uni_points(a, b, shards)
    ylist_func = [func(x) for x in xlist]
    ylist_interp = [intrplt_pol_for_func_uni(func, a, b, n, x) for x in xlist]
    y_list_diff = [abs(ylist_func[i] - ylist_interp[i]) for i in range(0, shards)]
   
    return max(y_list_diff)

def find_max_chebushev(func, a, b, n):
    xlist = gen_uni_points(a, b, shards)
    ylist_func = [func(x) for x in xlist]
    ylist_interp = [intrplt_pol_for_func_cheb(func, a, b, n, x) for x in xlist]
    y_list_diff = [abs(ylist_func[i] - ylist_interp[i]) for i in range(0, shards)]
   
    return max(y_list_diff)

# task A
x0 = 100
file = open('result.txt', 'w')

n = 5
draw_diff_chart(fs, x0 - 5, x0 + 5, n, file)

n = 10
draw_diff_chart(fs, x0 - 5, x0 + 5, n, file)

n = 15
draw_diff_chart(fs, x0 - 5, x0 + 5, n, file)

file.close()

# task B
x_list_diff = [i for i in range(5, 51)]
y_list_diff = [find_max(fs, x0 - 5, x0 + 5, nt) for nt in x_list_diff]
 
pylab.clf()
pylab.plot(x_list_diff, y_list_diff, 'b')
pylab.savefig("f1_diff.png")


x_list_diff_log = [i for i in range(5, 51)]
y_list_diff_log = [math.log10(find_max(fs, x0 - 5, x0 + 5, nt)) for nt in x_list_diff_log]
 
pylab.clf()
pylab.plot(x_list_diff_log, y_list_diff_log, 'b')
pylab.savefig("f1_diff_log.png")

# task C
x_list_diff2 = [i for i in range(5, 51)]
y_list_diff2 = [find_max_chebushev(fs, x0 - 5, x0 + 5, nt) for nt in x_list_diff2]

pylab.clf()
pylab.plot(x_list_diff2, y_list_diff2, 'b')
pylab.savefig("f1_diff_cheb.png")


x_list_diff2_log = [i for i in range(5, 51)]
y_list_diff2_log = [math.log10(find_max_chebushev(fs, x0 - 5, x0 + 5, nt)) for nt in x_list_diff2_log]

pylab.clf()
pylab.plot(x_list_diff2_log, y_list_diff2_log, 'b')
pylab.savefig("f1_diff_cheb_log.png")


# task D
x_list_diff3 = [i for i in range(5, 51)]
y_list_diff3 = [find_max(fm, 0, 2, nt) for nt in x_list_diff3]
 
pylab.clf()
pylab.plot(x_list_diff3, y_list_diff3, 'b')
pylab.savefig("f2_diff.png")

x_list_diff3_log = [i for i in range(5, 51)]
y_list_diff3_log = [math.log10(find_max(fm, 0, 2, nt)) for nt in x_list_diff3_log]
 
pylab.clf()
pylab.plot(x_list_diff3_log, y_list_diff3_log, 'b')
pylab.savefig("f2_diff_log.png")


x_list_diff4 = [i for i in range(5, 51)]
y_list_diff4 = [find_max_chebushev(fm, 0, 2, nt) for nt in x_list_diff4]

pylab.clf()
pylab.plot(x_list_diff4, y_list_diff4, 'b')
pylab.savefig("f2_diff_cheb.png")

x_list_diff4_log = [i for i in range(5, 51)]
y_list_diff4_log = [math.log10(find_max_chebushev(fm, 0, 2, nt)) for nt in x_list_diff4_log]

pylab.clf()
pylab.plot(x_list_diff4_log, y_list_diff4_log, 'b')
pylab.savefig("f2_diff_cheb_log.png")








