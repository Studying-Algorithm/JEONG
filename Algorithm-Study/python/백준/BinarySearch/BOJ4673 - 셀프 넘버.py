import sys

input = sys.stdin.readline

num = list(range(0, 10001))
removeArr = []

for n in num:
    for t in str(n):
        n += int(t)
    if n <= 10000:
        removeArr.append(n)

for n in removeArr:
    try:
        num.remove(n)
    except:
        continue

for n in num:
    print(n)