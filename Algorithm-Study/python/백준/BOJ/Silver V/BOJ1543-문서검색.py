import sys

input = sys.stdin.readline
str = input().strip()
word = input().strip()
i = 0
res = 0

while True:
    if len(str) < len(word):
        break
    index = str.find(word)
    if str[index:len(word)] == word:
        str = str[index+len(word):]
        res += 1
    else:
        str = str[1:]
print(res)