import sys

input = sys.stdin.readline
n = int(input())
isO = False

for _ in range(n):
    res = 0
    i = 0
    test = input()

    while i < len(test):
        if test[i] == 'O':
            res += 1
            j = 1
            isO = True
            while test[i + 1] == 'O' and isO == True:
                i += 1
                j += 1
                res += j
            isO = False
        i += 1
    print(res)
