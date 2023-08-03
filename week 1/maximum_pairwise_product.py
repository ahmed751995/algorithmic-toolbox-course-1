def max_pairwise(numbers):
    mx, s_mx = -1, -1
    for n in numbers:
        if n >= mx:
            s_mx = mx
            mx = n
        elif n > s_mx:
            s_mx = n
    return s_mx * mx


t = int(input())
numbers = map(int, input().split())

print(max_pairwise(numbers))
