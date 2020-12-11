def srch(i, j, ist, jst, rng, inp):
    for k in range(1, 1 + rng):
        ni = i + (ist * k); nj = j + (jst * k)
        if not 0 <= ni < len(inp) or not 0 <= nj < len(inp[0]): return False
        elif inp[ni][nj] == "#": return True
        elif inp[ni][nj] == "L": return False
    return False


def get_neighbours(i, j, inp, imm):
    rng = 1 if imm else len(inp) + len(inp[0])
    occ = 0
    occ += srch(i, j,  0,  1, rng, inp)
    occ += srch(i, j,  0, -1, rng, inp)
    occ += srch(i, j,  1,  0, rng, inp)
    occ += srch(i, j, -1,  0, rng, inp)
    occ += srch(i, j,  1,  1, rng, inp)
    occ += srch(i, j,  1, -1, rng, inp)
    occ += srch(i, j, -1,  1, rng, inp)
    occ += srch(i, j, -1, -1, rng, inp)
    return occ

def step(old, lim, imm):
    new = []
    updated = False
    for i,row in enumerate(old):
        new_row = list(row)
        for j,c in enumerate(row):
            ns = get_neighbours(i,j,old,imm)
            if c=="#":
                if ns >= lim:
                    new_row[j] = "L"
                    updated = True
            elif c=="L":
                if ns == 0:
                    new_row[j] = "#"
                    updated = True
        new.append("".join(new_row))
    return new, updated

def get_count(inp, sensitivity, immediate):
    ninp = inp.copy()
    upd = True
    while upd:
        ninp, upd = step(ninp, sensitivity, immediate)
    return sum(x.count("#") for x in ninp)

if __name__ == "__main__":
    inp = [l.strip() for l in open("input.txt").readlines() if len(l) > 1]
    print(get_count(inp, 4, True))
    print(get_count(inp, 5, False))
