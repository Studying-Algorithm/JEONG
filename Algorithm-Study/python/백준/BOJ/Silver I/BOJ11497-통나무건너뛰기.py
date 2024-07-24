import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    max = 0
    for i in range(n - 2):
        if max < abs(arr[i] - arr[i + 2]):
            max = abs(arr[i] - arr[i + 2])
    print(max)