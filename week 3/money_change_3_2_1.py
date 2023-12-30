#3.2.1
def money_change(n):
    return n//10 + (n%10)//5 + n%5

n = int(input())
print(money_change(n))
