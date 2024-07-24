import sys

input = sys.stdin.readline

def lotto(check, arr, index, cnt):
    if cnt == 6:
        print(*check)
        return
    for i in range(index, len(arr)):
        check[cnt] = arr[i]
        lotto(check, arr, i + 1, cnt + 1)

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    check = [0] * 6
    lotto(check, arr[1:], 0, 0)
    print()