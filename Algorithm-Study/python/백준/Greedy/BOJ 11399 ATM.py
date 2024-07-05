import sys

input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))
sum = 0
res = 0

P.sort()
for i in range(N):
    sum += P[i]
    res += sum
    
print(res)