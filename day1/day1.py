if __name__ == "__main__":
    expenses = sorted(map(lambda x : int(x.strip()), open("input.txt", 'r').readlines()))
    target = 2020

    # 2 at a time
    found = False
    for x in expenses:
        for y in expenses:
            if x + y == target:
                found = True
            elif x + y > target:
                break
            if found:
                break
        if found:
            break
    print(x,y,x*y)


    # 3 at a time
    found = False
    for x in expenses:
        for y in expenses:
            for z in expenses:
                if x + y + z == target:
                    found = True
                elif x + y + z > target:
                    break
                if found:
                    break
            if x + y > target:
                    break
            if found:
                break
        if found:
            break
    print(x,y,z,x*y*z)


