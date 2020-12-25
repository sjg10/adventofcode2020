def transform(subject, loop_size):
    num = 1
    for i in range(loop_size): num = num * subject % 20201227
    return num

def transform_search(subject, target):
    loop = 0
    num = 1
    while True:
        loop += 1
        num *= subject
        num %= 20201227
        if num == target: return loop

pk1=16616892
pk2=14505727

lc2=transform_search(7,pk2)
print(transform(pk1,lc2))



