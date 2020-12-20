from math import sqrt

class Tile:
    def __init__(self, lines):
        self.id = int(lines[0].split()[-1][:-1])
        self.size = len(lines[1].strip()) - 1
        self.ones = []
        self.rot = 0
        self.sides = [set(), set(), set(), set()]
        self.flipped = False
        for y,l in enumerate(lines[1:]):
            for x,c in enumerate(l.strip()):
                if c == "#":
                    self.ones.append([x,y])
                    if y == 0: self.sides[0].add(x)
                    if x == self.size: self.sides[1].add(y)
                    if y == self.size: self.sides[2].add(self.size - x)
                    if x == 0: self.sides[3].add(self.size - y)
    def __repr__(self):
        return str(self.id) + ": " + str(len(self.ones))
    def find_pot_nbors(self,tiles):
        self.matches = [None,None,None,None]
        self.fmatches = [None,None,None,None]
        for tile in tiles:
            if tile.id == self.id: continue
            for i, side in enumerate(self.sides):
                flipped_side = set(self.size - x for x in side)
                if flipped_side in tile.sides: 
                    assert(self.matches[i] is None)
                    assert(self.fmatches[i] is None)
                    self.matches[i] = tile.id
                if side in tile.sides:
                    assert(self.matches[i] is None)
                    assert(self.fmatches[i] is None)
                    self.fmatches[i] = tile.id
        self.corner = None
        for i in range(4):
            c = (self.matches[i] is None) and (self.matches[i - 1] is None) \
                    and (self.fmatches[i] is None) and (self.fmatches[i - 1] is None)
            if c: self.corner = i # i.e. != 0 and external sides are corner, corner - 1
    def rotate(self, turns): #clockwise
        for i in range(turns):
            self.fmatches.insert(0, self.fmatches.pop())
            self.matches.insert(0, self.matches.pop())
            self.sides.insert(0, self.sides.pop())
        self.rot += turns
        self.rot %= 4
    def flip(self):
        assert(not self.flipped) # cannot reverse
        assert(self.rot == 0) # cannot flip after rotate
        # use horizantal axis
        self.flipped = True
        oldmatches = self.matches
        oldfmatches = self.fmatches
        self.matches  = [oldfmatches[2], oldfmatches[1], oldfmatches[0], oldfmatches[3]]
        self.fmatches = [ oldmatches[2],  oldmatches[1],  oldmatches[0],  oldmatches[3]]
        newsides = [set(self.size - i for i in s ) for s in self.sides]
        self.sides = [newsides[2], newsides[1], newsides[0], newsides[3]]
    def get_picture_ones(self,strip_border):
        self.s_ones = []
        #image is flipped then rotated
        for l in self.ones:
            if self.flipped: l[1] = self.size - l[1]
            for i in range(self.rot):
                t = l[0]
                l[0] = self.size - l[1]
                l[1] = t
                pass
            if strip_border:
                if 0 < l[0] < self.size and 0 < l[1] < self.size:
                    self.s_ones.append([l[0] - 1, l[1] - 1])
            else:
                self.s_ones.append(l)

        return self.s_ones

def get_next_tile(tiles, last_tile_id, direction):
    t = tiles[last_tile_id]
    new_id = t.matches[direction]
    if new_id is None:
        new_id = t.fmatches[direction]
        tiles[new_id].flip()
    nt = tiles[new_id]
    old_side = t.sides[direction]
    ms = nt.sides.index(set(t.size - i for i in old_side))
    opp_dir = (direction + 2) % 4
    rots = (opp_dir + (4 - ms)) % 4
    nt.rotate(rots)
    return new_id


def build_grid(tiles, corners, grid_size):
    grid = [[0] * grid_size for i in range(grid_size)]
    # arrange top left corner
    # do top row:
    for y in range(grid_size):
        if y == 0:
            grid[0][0] = corners[0]
            t = tiles[corners[0]]
            #TODO: we get lucky here for our code that we dont need to flip/rotate/chose a different starting corner
            # it would be better to generalise so that we can find monsters! Possibly just by repeating search for all
            # monster orientations until one is found, rather than worrying here
            rots = 4 - t.corner % 4
            t.rotate(rots)
        else:
            grid[y][0] = get_next_tile(tiles, grid[y - 1][0],2)
        for x in range(1, grid_size):
            grid[y][x] = get_next_tile(tiles, grid[y][x - 1], 1)
    return grid

def extract_image(tiles, corners, grid, strip_border = False):
    tile_size = tiles[corners[0]].size - (1 if strip_border else -1) # exclude border
    size = tile_size * len(grid)
    out = [[0] *size for i in range(size)]
    for y, r in enumerate(grid):
        for x,tid in enumerate(r):
            ones = tiles[tid].get_picture_ones(strip_border)
            for xp,yp in ones:
                out[(y*tile_size) + yp][(x * tile_size) + xp] = 1
    return out,tile_size

def parse_monster(monster_str):
    monster = []
    for y,l in enumerate(monster_str):
        for x,c in enumerate(l):
            if c == "#": monster.append([x,y])
    return monster

def monster_search(image, monster):
    monster_tiles = set()
    for y,row in enumerate(image):
        for x,c in enumerate(row):
            fail = False
            points = set()
            for xp,yp in monster:
                xpp = x + xp
                ypp = y + yp
                points.add((xpp,ypp))
                if not (0 <=  xpp < len(image) and 0 <= ypp < len(image)):
                    fail = True
                    break
                if image[x + xp][y + yp] != 1:
                    fail = True
                    break
            if not fail:
                monster_tiles |= points
    return monster_tiles

monster_str="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")

if __name__== "__main__":
    # Load tiles
    with open("input.txt") as fd:
        tiles = {}
        lines = []
        for l in fd:
            if len(l) <= 1:
                t = Tile(lines)
                tiles[t.id] = t
                lines = []
            else:
                lines.append(l)

    # find their matching orientations and corners
    corners = []
    for t in tiles.values():
        t.find_pot_nbors(tiles.values())
        if t.corner is not None: corners.append(t.id)
    assert(len(corners) == 4)

    #corner id
    print(corners[0] * corners[1] * corners[2] * corners[3])
    
    #fit them in a grid, expand into an image
    grid_edge = int(sqrt(len(tiles)))
    grid  = build_grid(tiles, corners, grid_edge)
    img,tile_size = extract_image(tiles,corners,grid, True)

    #look for monsters
    monsters = parse_monster(monster_str)
    mtiles = monster_search(img, monsters)
    s = 0
    for y,row in enumerate(img):
        for x,c in enumerate(row):
            if c == 1:
                s += 1
    print(s - len(mtiles))



