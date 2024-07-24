import sys

input = sys.stdin.readline
A, B = input().split()
A = int(''.join(reversed(A)))
B = int(''.join(reversed(B)))

if A > B:
    print(A)
else:
    print(B)