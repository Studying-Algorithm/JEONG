import sys

def count(arr):
    sum = 0
    for i in range(len(arr)):
        if i == 0:
            sum += arr[1] - arr[0]
        elif i == len(arr) - 1:
            sum += arr[len(arr) - 1] - arr[len(arr) - 2]
        else:
            if arr[i + 1] - arr[i] >= arr[i] - arr[i - 1]:
                sum += arr[i] - arr[i - 1]
            else:
                sum += arr[i + 1] - arr[i]
    return sum


input = sys.stdin.readline
N = int(input())
arr = []
res = 0

for _ in range(N):
    x, y = map(int, input().split())
    arr.append([y, x])

arr.sort()
i = arr[-1][0]

for i in range(1, arr[-1][0] + 1):
    tmp = []
    for j in range(N):
        if arr[j][0] == i:
            tmp.append(arr[j][1])
    res += count(tmp)

print(res)