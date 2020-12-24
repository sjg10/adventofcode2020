def parse_tile(s):
    # use cube coordinates, x+y+z=0
    loc = [0,0,0]
    ptr = 0
    while ptr < len(s) and s[ptr]:
        if s[ptr] == "n":
            ptr+=1
            if s[ptr] == "e":
                loc[0] += 1
                loc[2] -= 1
            elif s[ptr] == "w":
                loc[1] += 1
                loc[2] -= 1
            else: assert(False)
        elif s[ptr] == "s":
            ptr+=1
            if s[ptr] == "e":
                loc[1] -= 1
                loc[2] += 1
            elif s[ptr] == "w":
                loc[0] -= 1
                loc[2] += 1
            else: assert(False)
        elif s[ptr] == "e":
            loc[0] += 1
            loc[1] -= 1
        elif s[ptr] == "w":
            loc[0] -= 1
            loc[1] += 1
        elif s[ptr] == "\n": pass # ignore newlines
        else: assert(False)
        ptr += 1
    return tuple(loc)

def permute(blacks):
    black_nbors = {}
    newblacks = []
    for t in blacks:
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    nl = (t[0] + i, t[1] + j, t[2] + k)
                    if i == j == k == 0: continue
                    if nl[0] + nl[1] + nl[2] == 0:
                        cnt = black_nbors.get(nl,0)
                        black_nbors[nl] = cnt + 1
    for t in black_nbors:
        black =  t in blacks
        cnt = black_nbors[t]
        if black and (cnt == 1 or cnt == 2): newblacks.append(t)
        if not black and cnt == 2: newblacks.append(t)
    return newblacks

if __name__ == "__main__":
    flipped = {}
    for l in open("input.txt").readlines(): 
        t = parse_tile(l)
        black = flipped.get(t,False)
        flipped[t] = not black
    blacks = [t for t in flipped if flipped[t]]
    print(len(blacks))

    for i in range(100):
        blacks = permute(blacks)
    print(len(blacks))
