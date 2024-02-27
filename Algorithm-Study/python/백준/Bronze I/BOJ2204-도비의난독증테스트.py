while True:
    n = int(input())
    arr = []
    copyArr = []

    if n == 0:
        break
    for i in range(n):
        arr.append(input())

    arr.sort(key=str.lower)
    print(arr[0])