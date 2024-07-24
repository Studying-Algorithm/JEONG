w = []
k = []

for i in range(10):
    w.append(int(input()))

for i in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

wScore = 0
kScore = 0

for i in range(0, 3):
    wScore += w[i]
    kScore += k[i]

print(wScore, kScore)