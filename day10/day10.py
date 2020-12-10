def calc_diffs(lines):
    sinp = sorted([int(x) for x in lines])
    d = [0,0,0,0] # number of 0,1,2,3 step sizes
    inp = [0] + sinp + [sinp[-1] + 3] # input with wall and device added
    ways = [0] * len(inp) # number of ways pos i can be reached from previous
    ways[0] = 1
    for i in range(1, len(inp)):
        for j in range(3): # Check the 3 preceeding for closeness
            a = i - (j+1) 
            if a >= 0:
                diff = inp[i] - inp[a]
                if diff in [1,2,3]: # if preceeding element was close - count the number of ways up
                    ways[i] += ways[a]
        d[inp[i] - inp[i-1]] += 1 # increment step size count
    return d,ways[-1]

with open("input.txt") as fd:
    rl = fd.readlines()

d,w = calc_diffs(rl)
print(d[3] * d[1],w)
