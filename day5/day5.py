def extract_seat(s): return int(s.translate(str.maketrans("BFRL","1010")), 2)

if __name__=="__main__":
    with open("input.txt") as fd:
        seats = sorted(list(map(extract_seat,fd)))
    en = enumerate(seats); next(en)
    for i,x in en:
        if x - 1 != seats[i - 1]: break
    print(seats[-1], x - 1) # max seat, missing seat
