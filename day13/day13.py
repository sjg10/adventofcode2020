def earliest(arrival, buses):
    a = int(arrival)
    bs = [int(x) for x in buses.split(",") if x != "x"]
    times = [(x,a + (x - (a % x))) for x in bs]
    res = min(times, key=lambda x: x[1])
    return res[0] * (res[1] - a)

def contest(buses):
    """
    We find the solution by noting that:
    If a bus with period p arrives at the correct number of minutes after t,
    it will repeat this occurence exactly every p minutes,
    but as all periods are coprime, if a bus with period p2 also arrives the correct
    number of minutes after t, the next time both will occur is in p*p2 minutes.
    """
    bs = [[i,int(x)] for i,x in enumerate(buses.split(",")) if x != "x"]
    incr = 1
    t = 0
    k = 0
    while k < len(bs): #Using the above we find t by fixing one bus at a time.
        if (t + bs[k][0]) % bs[k][1] == 0:
            incr *= bs[k][1]
            k += 1
        else:
            t += incr
    return t

if __name__=="__main__":
    with open("input.txt") as fd:
        arrival = fd.readline()
        buses = fd.readline()
    print(earliest(arrival, buses))
    print(contest(buses))
