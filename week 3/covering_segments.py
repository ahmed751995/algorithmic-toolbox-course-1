def covering_segments(ar):
    ar.sort(key=lambda x: x[0])
    lines = []
    line = ar[0]
    p = line[0]
    for l in ar[1:]:
        if line[0]<= l[0] <= line[1]:
            p = max(line[0], l[0])
            line = [max(line[0], l[0]), min(line[1], l[1])]
        else:
            lines.append(p)
            p = l[0]
            line = l
    lines.append(p)
    return lines


n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

lines = covering_segments(l)
print(len(lines))
lines = list(map(str, lines))
print(' '.join(lines))
