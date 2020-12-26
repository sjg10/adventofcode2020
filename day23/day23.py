class Game:
    def __init__(self, cupstr, fill = 0):
        cupint = [int(c) for c in cupstr]
        self.first=cupint[0]
        self.cups = {}
        for i,c in enumerate(cupint[1:]):
            self.cups[cupint[i]] = c
        self.cups[cupint[-1]] = cupint[0]
        self.cur_cup = cupint[0]
        last = cupint[-1]
        l = len(self.cups)
        for i in range(l, fill):
            self.cups[last] = i + 1
            last = i + 1
            self.cups[i + 1] = cupint[0]
    def move(self, moved, src, dest):
        srcr = self.cups[dest]
        self.cups[src] = self.cups[moved[-1]]
        self.cups[dest] = moved[0]
        self.cups[moved[-1]] = srcr
    def step(self):
        extracted = []
        nxt = self.cur_cup
        for i in range(3): 
            nxt = self.cups[nxt]
            extracted.append(nxt)
        d = self.cur_cup - 1
        if d == 0: d = len(self.cups)
        for i in range(len(extracted)):
            if d in extracted:
                d -= 1
                if d == 0: d = len(self.cups)
            else: break
        self.move(extracted, self.cur_cup, d)
        self.cur_cup = self.cups[self.cur_cup]
    def get_cw_one(self):
        a = self.cups[1] 
        b = self.cups[a]
        return a*b
    def __repr__(self):
        s = ""
        n = self.cups[1]
        for i in range(len(self.cups) - 1):
            s += str(n)
            n = self.cups[n]
        return s


if __name__ == "__main__":
    gstr = "398254716"
    g = Game(gstr)
    for i in range(100):
        g.step()
    print(g)

    g = Game(gstr, 1000000)
    for i in range(10000000):
        g.step()
    print(g.get_cw_one())
