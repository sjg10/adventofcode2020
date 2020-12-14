def read_mask(line):
    ms = line.split(" = ")[1].strip()
    set_msk = 0
    clr_msk = 0
    floating_msk = []
    for i  in range(len(ms)):
        if ms[i] == "0": clr_msk |= (2** (len(ms) - (i + 1)))
        elif ms[i] == "1": set_msk |= (2** (len(ms) - (i + 1)))
        elif ms[i] == "X": floating_msk.append(2**(len(ms) - (i + 1)))

    return set_msk, clr_msk, floating_msk

def read_ins_v1(mask,line):
    s = line.split("] = ")
    maddr = int(s[0].split("[")[-1])
    mval = int(s[1])
    mval |= mask[0]
    mval &= ~mask[1]
    return [maddr],mval

def read_ins_v2(mask,line):
    s = line.split("] = ")
    maddr = int(s[0].split("[")[-1])
    mval = int(s[1])
    maddr |= mask[0]
    addrs = []
    for y in range(2 ** len(mask[2])):
        # Loop through all possible combinations of mask[2]'s
        z = y
        addr = maddr
        for m in mask[2]:
            if z & 1: addr |= m
            else: addr &= ~m
            z >>= 1
        addrs.append(addr)
    return addrs, mval

def run(lines, parser):
    mem= {}
    mask = [0,0,0]
    for l in lines:
        if l[:4] == "mask": mask = read_mask(l)
        elif l[:3] == "mem":
            maddr,mval = parser(mask, l)
            for addr in maddr: mem[addr] = mval
    return sum(mem.values())

if __name__ == "__main__":
    with open("input.txt") as fd:
        print(run(fd, read_ins_v1))

    with open("input.txt") as fd:
        print(run(fd, read_ins_v2))
