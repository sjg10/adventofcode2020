def run(lines):
    acc = 0
    skip = 0
    ptr = 0
    halt = False
    repeat = False
    ran = set()
    while not (halt or repeat):
        s = lines[ptr].split()
        ran.add(ptr)
        ins = s[0]; num = int(s[1])
        if ins == "nop": pass
        if ins == "acc": acc += num
        if ins == "jmp": ptr += num
        else: ptr += 1
        repeat = ptr in ran
        halt = (ptr >= len(lines))
    return acc, halt

def search(lines):
    for i,l in enumerate(lines):
        tmpprg = prog.copy()
        if l[:3] == "nop": tmpprg[i] = tmpprg[i].replace("nop","jmp")
        elif l[:3] == "jmp": tmpprg[i] = tmpprg[i].replace("jmp", "nop")
        else: continue
        acc, halt = run(tmpprg)
        if halt: break
    return acc, halt


with open("input.txt") as fd:
    prog = fd.readlines()

print(run(prog))
print(search(prog))
