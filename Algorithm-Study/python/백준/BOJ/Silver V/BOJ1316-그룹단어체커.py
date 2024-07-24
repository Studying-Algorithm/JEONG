import sys

input = sys.stdin.readline
n = int(input())
res = 0

def check(word):
    for i in range(len(word)):
        for j in range(len(word)):
            if word[i] == word[j]:
                if j - i > 1:
                    if word[j] != word[j - 1]:
                        return 0
    return 1

for _ in range(n):
    word = input()
    res += check(word)
print(res)