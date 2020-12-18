def calc(s):
    return _calc(s, calc_flat_lr)[0]

def calc_adv(s):
    return _calc(s, calc_flat_adv)[0]

def calc_flat_lr(nums_l, ops_l):
    x = nums_l[0]
    for i,op in enumerate(ops_l):
        if   op == "+": x+= nums_l[i+1]
        elif op == "*": x*= nums_l[i+1]
    return x
    

def calc_flat_adv(nums_l, ops_l):
    ops = {"*": lambda x,y: x*y,"+": lambda x,y: x+y}
    x = nums_l[0]
    mul_nums = []
    while True:
        try: 
            idx = ops_l.index("+")
            ops_l.pop(idx)
            a = nums_l.pop(idx)
            nums_l[idx] += a
        except ValueError: break
    m = 1
    for x in nums_l: m *= x
    return m
    


def _calc(s, flat_fn):
    nums_l = []
    ops_l = []
    enum = enumerate(s)
    ptr = 0
    for ptr,c in enum:
        if c in ["*","+"]: ops_l.append(c)
        elif c == "(": 
            recres = _calc(s[ptr + 1:], flat_fn)
            nums_l.append(recres[0])
            for i in range(recres[1]): next(enum)
        elif c == ")": break
        elif c == " ": continue
        else: nums_l.append(int(c))
    x = flat_fn(nums_l, ops_l)
    return x, ptr + 1

if __name__ == "__main__":
    with open("input.txt") as fd:
        print(sum(calc(l.strip()) for l in fd))
    with open("input.txt") as fd:
        print(sum(calc_adv(l.strip()) for l in fd))
