n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()

for i, j in arr:
    print(i, j)