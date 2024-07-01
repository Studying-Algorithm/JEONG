import sys

input = sys.stdin.readline
E, S, M = map(int, input().split())
e = s = m = 0
year = 0

while True:
    if E==e and S==s and M==m:
        break
    else:
        e += 1
        s += 1
        m += 1
        year += 1
        if e > 15:
            e = 1
        if s > 28:
            s = 1
        if m > 19:
            m = 1
print(year)