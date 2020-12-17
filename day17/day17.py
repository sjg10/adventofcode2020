from itertools import product
def cycle(active_cubes):
    dims = len(active_cubes[0])
    mins = [0] * dims
    maxs = [0] * dims
    new_active_cubes = []
    for c in active_cubes:
        for i in range(dims):
            if c[i] > maxs[i]: maxs[i] = c[i]
            elif c[i] < mins[i]: mins[i] = c[i]
    rs = [range(mins[i] - 1, maxs[i] + 2) for i in range(dims)]
    for tc in product(*rs):
        nbors = 0
        active = False
        for c in active_cubes:
            if all(tc[i] - 1 <= c[i] <= tc[i] + 1 for i in range(dims)):
                if c == tc: active = True
                else: nbors += 1
        if (active and nbors in [2,3]) or \
           (not active and nbors == 3):
            new_active_cubes.append(tc)
    return new_active_cubes

def load(lines,dims):
    active_cubes = []
    for y,l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#": active_cubes.append((x,y) + (0,) * (dims - 2))
    return active_cubes

def run(inp, dims, cycles):
    a = load(inp,dims)
    print(0, len(a))
    for i in range(cycles):
        a = cycle(a)
        print(i + 1, len(a))
    return len(a)

if __name__ == "__main__":
    with open("input.txt") as fd:
        inp = fd.readlines()

    print("dims", 3, "res", run(inp,3,6))
    print("dims", 4, "res", run(inp,4,6))
