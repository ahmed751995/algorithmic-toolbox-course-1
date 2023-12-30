from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x: return 1
    elif y + x > x + y: return -1
    else: return 0


n = int(input())
a = input().split()
a.sort(key=cmp_to_key(compare), reverse=True)
print(''.join(a))

# def largest_number(numbers):
#     for _ in numbers:
#         for i in range(len(numbers) - 1):
#             if numbers[i] + numbers[i + 1] < numbers[i + 1] + numbers[i]:
#                 t = numbers[i]
#                 numbers[i] = numbers[i + 1]
#                 numbers[i + 1] = t
#     return int(''.join(numbers))

# if __name__ == '__main__':
#     _ = int(input())
#     input_numbers = input().split()
#     print(largest_number(input_numbers))

