class Game():
    def __init__(self, gamestr):
        self.numbers = [int(x) for x in gamestr.split(",")]
        self.counts = {}
        self.turn = 0
        self.last_number = None
        self.last_number_turn = None
    def move(self):
        self.turn += 1
        if self.turn - 1 < len(self.numbers):
            self.last_number = self.numbers[self.turn - 1]
        elif not self.last_number_turn:
            self.last_number = 0
        else:
            self.last_number = (self.turn - 1) - self.last_number_turn
        self.last_number_turn = self.counts.get(self.last_number)
        self.counts[self.last_number] = self.turn
        return self.last_number


g = Game("0,14,1,3,7,9")
for i in range(2020):
    t = g.move()
print(t)
for i in range(30000000 - 2020):
    t = g.move()
print(t)
