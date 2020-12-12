def step(pos, bearing, instruction):
    dr = instruction[0]
    cnt = int(instruction[1:])
    if   dr == "F": dr = ["E", "N", "W", "S"][bearing // 90]
    if   dr == "N": pos[1] += cnt
    elif dr == "S": pos[1] -= cnt
    elif dr == "E": pos[0] += cnt
    elif dr == "W": pos[0] -= cnt
    elif dr == "L": bearing += cnt
    elif dr == "R": bearing -= cnt
    return pos, bearing % 360

def step_way(pos, way_pos, instruction):
    dr = instruction[0]
    cnt = int(instruction[1:])
    if dr == "F": 
        pos[0] += way_pos[0] * cnt
        pos[1] += way_pos[1] * cnt
    elif dr == "N": way_pos[1] += cnt
    elif dr == "S": way_pos[1] -= cnt
    elif dr == "E": way_pos[0] += cnt
    elif dr == "W": way_pos[0] -= cnt
    elif dr == "L":
        for i in range(cnt // 90):
            t = way_pos[0]
            way_pos[0] = -way_pos[1]
            way_pos[1] = t
    elif dr == "R":
        for i in range(cnt // 90):
            t = way_pos[0]
            way_pos[0] = way_pos[1]
            way_pos[1] = -t
    return pos, way_pos

if __name__ == "__main__":
    lines = open("input.txt").readlines()

    pos = [0,0]
    bearing = 0
    for l in lines:
        pos, bearing = step(pos,bearing,l)
    print(abs(pos[0]) + abs(pos[1]))

    pos = [0,0]
    way_pos = [10, 1]
    for l in lines:
        pos, way_pos = step_way(pos, way_pos, l)
    print(abs(pos[0]) + abs(pos[1]))


        
