def find_1(int_arr, preamble_length):
    preamble = int_arr[:preamble_length]
    valid_sums = [a + b for a in preamble for b in preamble if a != b]
    for i in int_arr[preamble_length:]:
        sums =  [a + b for a in preamble for b in preamble if a != b]
        if i not in sums:
            return i
        preamble.pop(0)
        preamble.append(i)
    return None



def find_2(int_arr, summand):
    l = len(int_arr)
    for i in range(l):
        s = int_arr[i]
        for j in range(1,l - i):
            s += int_arr[i + j]
            if s == summand:
                return min(int_arr[i:i + j + 1]) +  max(int_arr[i: i + j + 1])
            elif s > summand: break

with open("input.txt") as fd:
    int_inp = [int(x) for x in fd.readlines()]
f = find_1(int_inp, 25)
ff = find_2(int_inp, f)
print(f,ff)
