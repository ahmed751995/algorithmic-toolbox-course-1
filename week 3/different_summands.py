def different_summands(x):
    s = 0
    l = []
    if x == 1:
        return ['1']
    for i in range(1, x):
        if x - (i + s) > i:
            s += i
            l.append(str(i))
        else:
            l.append(str(x - s))
            break
    return l

n = int(input())
s = different_summands(n)
print(len(s))
print(' '.join(s))
