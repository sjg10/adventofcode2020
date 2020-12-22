class Player:
    def __init__(self, cards):
        self.cards = cards
    def draw(self):
        return self.cards.pop(0)
    def win(self, mycard, theircard):
        self.cards.append(mycard)
        self.cards.append(theircard)
    def score(self):
        s = 0
        for l,c in enumerate(self.cards):
            s += c * (len(self.cards) - l)
        return s
    def lost(self):
        return len(self.cards) == 0
    def recursive_check(self, card):
        return len(self.cards) >= card
    def force_lose(self):
        self.cards.clear()


class Game:
    def __init__(self, gametext, depth=0, prev_rounds = []):
        self.rounds = prev_rounds
        self.depth = depth
        self.init_cards = {1: [], 2: []}
        self.players = {}
        player = 0
        for l in gametext:
            ls = l.strip()
            if ":" in l:
                player = int(ls.split()[1][:-1])
            elif len(ls) > 0:
                self.init_cards[player].append(int(ls))
        self.reset()
    def reset(self):
        self.rounds = []
        self.players[1] = Player(self.init_cards[1].copy())
        self.players[2] = Player(self.init_cards[2].copy())
        self.winner = None
        self.loser  = None
    def turns(self, recursive= False):
        cur_round = (self.players[1].cards.copy(), self.players[2].cards.copy())
        p1 = self.players[1].draw()
        p2 = self.players[2].draw()
        if recursive:
            if cur_round in self.rounds:
                self.players[2].force_lose()
                return 1,2
            self.rounds.append(cur_round)
            p1_r = self.players[1].recursive_check(p1)
            p2_r = self.players[2].recursive_check(p2)
            if p1_r and p2_r:
                g = Game("", self.depth + 1, self.rounds)
                g.players[1] = Player(self.players[1].cards.copy()[:p1])
                g.players[2] = Player(self.players[2].cards.copy()[:p2])
                w,l =  g.play(True)
                if w == 1: self.players[1].win(p1,p2)
                else: self.players[2].win(p2,p1)
                return w,l
            #otherwise fall through!
        assert(p1 != p2) # cant handle it!
        if p1 > p2: 
            self.players[1].win(p1, p2)
            return 1,2
        elif p2 > p1: 
            self.players[2].win(p2, p1)
            return 2,1
    def play(self, recursive = False):
        end = False
        rnd = 0
        while not end:
            winner,loser = self.turns(recursive)
            rnd += 1
            if self.players[loser].lost(): end = True
        self.winner = winner
        self.loser = loser
        return self.winner, self.loser
    def get_final_score(self):
            return self.players[self.winner].score()

if __name__ == "__main__":
    with open("input.txt") as fd:
        g = Game(fd.readlines())
    g.play()
    print(g.get_final_score())
    g.reset()
    g.play(True)
    print(g.get_final_score())
