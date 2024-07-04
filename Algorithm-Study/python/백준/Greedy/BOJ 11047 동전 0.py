import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coin = []
res = 0

for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

i = 0
while K > 0:
    if K == 1:
        res += 1
        break
    if K >= coin[i]:
        res += K // coin[i]
        K %= coin[i]
    else:
        i += 1

print(res)