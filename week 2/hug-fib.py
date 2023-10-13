def fib(n, m):
    fn = {0: 0, 1: 1}
    r = [0, 1]
    flag = 0
    for i in range(2, n + 1):
        fn[i] = fn[i - 1] + fn[i - 2]
        rt = fn[i] % m
        if r[-1] == 0 and rt == 1:
            flag = 1
            break
        r.append(rt)

    if flag:
        r.pop(-1)
    if n <= len(r):
        return sum(r[:n+1])
    else:
        mod = n % len(r) + 1
        return ((sum(r) * (n//len(r))) + (sum(r[:mod])))%10

st, ed = map(int, input().split())
if st > 0:
    print((fib(ed, 10) - fib(st - 1, 10)) % 10)
else:
    print((fib(ed, 10) - fib(st, 10)) % 10)
