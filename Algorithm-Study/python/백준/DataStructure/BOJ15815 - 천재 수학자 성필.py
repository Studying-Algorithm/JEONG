import sys

input = sys.stdin.readline

arr = input().strip()
numbers = []
result = []
a = 0
b = 0

for n in arr:
    if n.isdigit():
        numbers.append(int(n))
    else:
        b = numbers.pop()
        a = numbers.pop()

        if n == '+':
            result = a + b
        elif n == '-':
            result = a - b
        elif n == '*':
            result = a * b
        elif n == '/':
            result = a / b
        numbers.append(int(result))

print(numbers.pop())