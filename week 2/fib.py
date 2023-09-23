def fib(n):
    x ={0: 0 ,1: 1}
    for f in range(2, n + 1):
        x[f] = x[f - 1] + x[f - 2]
    return x[n]


if __name__ == "__main__":
    x = int(input())
    print(fib(x))
