import sys
import math

input = sys.stdin.readline
K = int(input())
limit = int(K * math.log(K) * 1.2) + 1  
arr = [1] * limit
arr[0] = 0
arr[1] = 0
cnt = 0

for i in range(2, limit):
    if arr[i]:
        cnt += 1
        if cnt == K:
            print(i)
            break
        for j in range(i * 2, limit, i):
            arr[j] = 0