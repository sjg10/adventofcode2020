from string import ascii_lowercase as letters

def run(src):
    su = 0; si = 0
    setu = set(); seti = set(letters)
    for l in src:
        ls = set(l.strip())
        if not len(ls):
            su+= len(setu); si+= len(seti)
            setu = set(); seti = set(letters)
        else:
            setu |= ls
            seti &= ls
    if len(setu): su+= len(setu); si+= len(seti)
    return su, si

with open("input.txt") as fd:
    print(run(fd))
