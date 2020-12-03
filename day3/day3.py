class SlopeGame:
    def __init__(self, mapiter):
        self.smap=[[y == '#' for y in x.strip()] for x in mapiter]
        self.xmax = len(self.smap[0])
        self.ymax = len(self.smap)
    def calc(self, right, down):
        self.slope = (down, right)
        self.loc = [0, 0]
        self.end = False
        self.count = 0
        while not self.end:
            self.step()
        return self.count
    def step(self):
        self.loc[0] += self.slope[0]
        self.loc[1] += self.slope[1]
        self.end = (self.loc[0] >= self.ymax)
        if not self.end: self.count += self.smap[self.loc[0]][self.loc[1] % self.xmax]



if __name__ == "__main__":
    with open("input.txt") as fd:
        g = SlopeGame(fd)
    t1 = g.calc(1,1)
    t2 = g.calc(3,1)
    t3 = g.calc(5,1)
    t4 = g.calc(7,1)
    t5 = g.calc(1,2)
    print(t1,t2,t3,t4,t5,t1*t2*t3*t4*t5)
