def parse_rule(line):
    sc = line.split(": ")
    field = sc[0]
    ranges = [x.split("-") for x in sc[1].split(" or ")]
    prange = []
    for a,b in ranges:
        prange+= list(range(int(a),int(b) + 1))
    return {field: prange}

def validate_ticket(line, rules):
    valids = []
    invalids = []
    classes = [set() for x in rules]
    for i,x in enumerate([int(y) for y in line.split(",")]):
        valid = False
        for field,rng in rules.items():
            if x in rng:
                valid |= x in rng
                classes[i].add(field)
        if valid:
            valids.append(x)
        else: invalids.append(x)
    return valids, invalids, classes

def parse_input(lines):
    rules = {}
    invalids = []
    valid_tickets = []
    my_ticket = True
    for line in lines:
        if "or" in line:
            rules.update(parse_rule(line))
        elif "your" in line:
            my_ticket = True
        elif "nearby" in line:
            my_ticket = False
            possible_classes = [set(rules.keys()) for x in rules]
        elif "," in line and not my_ticket:
            v,i,c = validate_ticket(line, rules)
            if len(i) == 0:
                for j,cs in enumerate(c):
                    possible_classes[j] &= cs
            invalids += i
            if len(invalids) == 0: valid_tickets.append(line)
        elif "," in line and my_ticket:
            my_ticket_line = line
    classes = finalise_possible_classes(possible_classes)
    return invalids, my_ticket_line, classes

def finalise_possible_classes(possible_classes):
    finished = False
    while sum(len(x) for x in possible_classes) != len(possible_classes):
        for cs in possible_classes:
            if len(cs) == 1:
                for c in cs: #a way of getting that item without popping
                    for cs2 in possible_classes:
                        if c in cs2 and cs2 != cs: cs2.remove(c)
    return [x.pop() for x in possible_classes]

def find_departure_number(my_ticket, classes):
    ds = 1
    mt = [int(x) for x in my_ticket.split(",")]
    for i,c in enumerate(classes):
        if "departure" in c:
            ds *= mt[i]
    return(ds)

with open("input.txt") as fd:
    invalids, my_ticket, classes = parse_input(fd)
print(sum(invalids))
print(find_departure_number(my_ticket, classes))
