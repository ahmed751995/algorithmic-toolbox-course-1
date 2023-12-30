def dot_product(l1, l2):
    l1.sort()
    l2.sort()
    s = 0
    for i in range(len(l1)):
        s += l1[i] * l2[i]
    return s

n = input()
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(dot_product(l1, l2))
