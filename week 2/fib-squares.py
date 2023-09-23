def mod_fib(n, m):
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
    return r[n % len(r)]

def fib_sum(n):
    fn = mod_fib(n, 10)
    fn_1 = mod_fib(n-1, 10)
    return (fn * (fn + fn_1)) % 10

n = int(input())
print(fib_sum(n))
