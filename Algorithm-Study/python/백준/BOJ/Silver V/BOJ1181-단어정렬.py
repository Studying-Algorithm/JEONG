import sys

input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    arr.append(input().strip())

arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for w in arr:
    print(w)