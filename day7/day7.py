def parse_rules(fd):
    d = {}
    for l in fd:
        ls = l.split(" bags contain ")
        lss = [x.split() for x in ls[1].split(",")]
        rule = {" ".join(x[1:3]): int(x[0]) for x in lss if x[0] != "no"}
        d[ls[0]] = rule
    return d


def find_bag(colour, rules):
    """
    Finds how many different coloured bags colour can be inside according to rules.
    """
    def find_in(in_col, out_col, examined):
        if out_col not in examined:
            r = rules[out_col]
            if in_col in r:  
                examined[out_col] = True
            elif len(r) > 0:
                for c in r:
                    if find_in(in_col, c, examined): 
                        examined[out_col] = True
                        break
                if out_col not in examined: examined[out_col] = False
            else: examined[out_col] = False
        return examined[out_col]
    count = 0
    examined = {}
    for out_col in rules:
            count += find_in(colour, out_col, examined)
    return count


def count_bags(col, rules, examined = {}):
    """
    Counts how many bags col contains according to rules. Uses examined dict for colours already counted
    """
    if col not in examined:
        c = 0
        for in_col,cnt in rules[col].items():
            c += cnt
            c += cnt * count_bags(in_col, rules, examined)
        examined[col] = c
    return examined[col]


rules = parse_rules(open("input.txt"))

print(find_bag("shiny gold", rules))
print(count_bags("shiny gold", rules))
