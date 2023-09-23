def fib_sum(st, ed):
    x = {0: 0, 1: 1}
    if ed == 1: return 1
    s = 0
    for f in range(2, ed + 1):
        x[f] = x[f - 1] + x[f - 2]
        if st <= f:
            s += x[f]
    return s % 10


st, ed = map(int, input().split())
print(fib_sum(st, ed))
