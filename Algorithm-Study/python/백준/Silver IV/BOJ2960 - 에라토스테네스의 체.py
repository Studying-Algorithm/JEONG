import sys
import math

input = sys.stdin.readline
N, K = map(int, input().split())
res = 0

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

arr = [ i for i in range(2, N + 1) ]

while K >= 0:
    n = min(arr)
    if isPrime(n):
        m = [ i for i in range(n, max(arr)+ 1, n) ]
        for i in m:
            if i in arr:
                if K <= 0:
                    break
                K -= 1
                res = i
                arr.remove(i)
    if K <= 0:
        break

print(res)