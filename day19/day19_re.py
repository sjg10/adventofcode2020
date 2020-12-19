import re
from copy import deepcopy
def initial_parse(lines):
    rules = {}
    ruleidx = 0
    text = []
    for l in lines:
        if len(l) <= 1: continue
        s = l.split(": ")
        if len(s) > 1:
            ruleidx = int(s[0])
            txt = s[1].split('"')
            if len(txt) > 1:
                rules[ruleidx] = txt[-2]
            else:
                rules[ruleidx] = []
                for x in s[1].split("|"):
                    opt = []
                    for i in x.split():
                        opt.append(int(i))
                    rules[ruleidx].append(opt)
        else:
            text.append(l.strip())
    return rules, text

def get_rule(ruleidx, rules, part2= False):
    if part2 and ruleidx == 8:
        r = get_rule(42,rules)
        return r + "+"
    if part2 and ruleidx == 11:
        r1 = get_rule(42,rules)
        r2 = get_rule(31,rules)
        rs = []
        for i in range(1,10): #TODO: more needed? - or better!
            rs.append(r1+"{" +str(i) + "}" + r2 + "{" + str(i) + "}")
        return "(" + "|".join(rs) + ")"
    rule = rules[ruleidx]
    if type(rule) is not str: #ie. not already regex:
        new_rules = []
        for r in rule:
            gen_rule = ""
            for s in r:
                if type(s) is int:
                    gen_rule += get_rule(s, rules, part2)
                else:
                    gen_rule += s
            new_rules.append(gen_rule)
        if len(new_rules) == 1:
            nr = new_rules[0]
        else:
            nr = "(" + "|".join(new_rules) + ")"
        rules[ruleidx] = nr
    return rules[ruleidx]

if __name__=="__main__":
    with open("input.txt") as fd:
        rules, text = initial_parse(fd.readlines())

    r = re.compile(get_rule(0,deepcopy(rules)))
    print(sum(1 for i in text if r.fullmatch(i)))

    r = re.compile(get_rule(0,deepcopy(rules),True))
    print(sum(1 for i in text if r.fullmatch(i)))
