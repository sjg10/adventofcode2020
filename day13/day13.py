from math import prod
from time import time as nw
from functools import reduce
from math import gcd

def lcm(x,y): return x * y // gcd(x,y)

def earliest(arrival, buses):
    a = int(arrival)
    bs = [int(x) for x in buses.split(",") if x != "x"]
    times = [(x,a + (x - (a % x))) for x in bs]
    res = min(times, key=lambda x: x[1])
    return res[0] * (res[1] - a)

def contest(buses, hint = 0):
    good = False
    bs = [(i,int(x)) for i,x in enumerate(buses.split(",")) if x != "x"]
    bs.sort(key=lambda b: b[1],reverse=True)
    t = hint
    while not good:
        good = True
        for k,b in bs:
            arr = (b - (t % b)) % b
            incr = (arr - k) % b
            if arr != k:
                good = False
                t += incr
                break
    print(t)


def contest(buses, hint = 0):
    good = False
    bs = [((int(x) - i) % int(x),int(x)) for i,x in enumerate(buses.split(",")) if x != "x"]
    bs.sort(key=lambda b: b[1],reverse=True)
    ts = bs[0][0] + (hint - (hint % bs[0][1]))
    t=ts
    mx = prod([x[1] for x in bs])
    p = 0
    st = nw()
    while not good:
        np = (t - ts)/(mx - ts) * 100
        if np - p > 0.001:
            p = np
            el = nw() - st
            rem =  el * (100/p) - el
            print("%.5f pc, %.5fs/%.5fs " % (p,el,rem))
        good = True
        for k,b in bs:
            if t % b != k:
                good = False
                t += bs[0][1]
                break
    print(t)

def red(bs):
    ds = [] #The number of multiples of bs[0] to increase time by to hit a matching time
    assert(bs[0][0] == 0) # TODO: handle non-zero
    for i in range(1,len(bs)):
        print(bs[i])
        # The increase in minutes after arrival of bus i for each bus 0 that arrives:
        s= bs[i][1] - bs[0][1] % bs[i][1]
        print("s",s)
        # Now find for each bus, after how many bus 0's does bus i have the correct minute offset:
        for d in range(1,bs[i][1]):
            if ((d * s) % bs[i][1]) == bs[i][0]:
                break
        print("d",d)
        ds.append(d)
    print(ds)
    return ds

def srch(bs, ds):
    k = ds[0]
    assert(bs[0][0] == 0) # TODO: handle non-zero
    good = False
    while not good:
        good = True
        for i in range(len(ds) - 1):
            if k % bs[i + 2][1] != ds[i + 1]:
                k += bs[1][1]
                good = False
                break
    return (k*bs[0][1] + bs[0][0])


def contest(buses, hint=0):
    bs = [(i,int(x)) for i,x in enumerate(buses.split(",")) if x != "x"]
    ds = red(bs)
    #Now that we have ds, we can search as below:
    print(srch(bs,ds)) # TODO: once non zero init allowed, iterated red func


with open("input.txt") as fd:
    arrival = fd.readline()
    buses = fd.readline()
#print(earliest(arrival, buses))
#contest("7,13,x,x,59,x,31,19")
contest("17,x,13,19",hint = 3000)
#contest("67,7,59,61")
#contest("1789,37,47,1889")
#contest(buses, 100000000000000)
