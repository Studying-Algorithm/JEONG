n, m = map(int, input().split())

nArr = []
mArr = []

for i in range(n):
    nArr.append(input())

for i in range(m):
    mArr.append(input())

nArr.sort()
mArr.sort()
intersection = list(set(nArr) & set(mArr))
intersection.sort()

print(len(intersection))
for word in intersection:
    print(word)