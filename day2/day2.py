def valid_old(p):
    s = p.split(":")
    cond = s[0].split(" ")
    inp = s[1].strip()
    r = cond[0].split("-")
    c = inp.count(cond[1])
    return int(r[0]) <= c <= int(r[1])

def valid_new(p):
    s = p.split(":")
    cond = s[0].split(" ")
    inp = s[1].strip()
    r = cond[0].split("-")
    a = (inp[int(r[0]) - 1] == cond[1])
    b = (inp[int(r[1]) - 1] == cond[1])
    return a ^ b

def check_pass(filename, validator):
    good = 0
    with open(filename) as fd:
        for l in fd:
            if validator(l):
                good += 1
    return good

if __name__ == "__main__":
    print(check_pass("input.txt",valid_old))
    print(check_pass("input.txt",valid_new))
