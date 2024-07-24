import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

res = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(5):
        for k in range(N):
            if arr[i][j] == arr[k][j]:
                res[i][k] = 1

ans = [0] * N
for i, s in enumerate(res):
    ans[i] = s.count(1)

print(ans.index(max(ans)) + 1)