from fib import fib as normal_fib

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
    return r[n % len(r)]

# for stress test
# import random
# for i in range(1000):
#     n = random.randint(1, 100000)
#     m = random.randint(1, 1000)
#     slow_fib = normal_fib(n)%m
#     fast_fib = fib(n, m)
#     print(f"{slow_fib} == {fast_fib}")
#     assert(slow_fib == fast_fib)


if __name__ == "__main__":
    n, m  = map(int, input().split())
    print(fib(n, m))
