import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

index = [arr[i][0] for i in range(N)].index(K)

for i in range(N):
    if arr[index][1:] == arr[i][1:]:
        print(i + 1)
        break