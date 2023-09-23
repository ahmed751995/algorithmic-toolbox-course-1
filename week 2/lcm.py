def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    g = gcd(a, b)
    l = (a * b) / g
    return int(l)

a, b = map(int, input().split())
print(lcm(a, b))
