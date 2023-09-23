def fib_sum(n):
    if n == 0:
        return 0
    x = {0: 0, 1: 1}
    s = 1
    for f in range(2, n + 1):
        x[f] = x[f - 1] + x[f - 2]
        s += x[f]
    return s % 10

n = int(input())
print(fib_sum(n))
