import sys

input = sys.stdin.readline
N = int(input())

def hanNum(n):
    res = 0
    if n < 100:
        return n
    else:
        for i in range(110, n + 1):
            arr = list(str(i))
            tmp = int(arr[0]) - int(arr[1])
            if int(arr[1]) - int(arr[2]) == tmp:
                res += 1
        return res + 99

print(hanNum(N))