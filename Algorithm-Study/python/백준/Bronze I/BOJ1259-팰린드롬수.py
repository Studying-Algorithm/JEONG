import sys

input = sys.stdin.readline

def pal(read):
    for i in range(len(read) // 2):
        if read[i] != read[len(read) - 1 - i]:
            return 0
    return 1

while True:
    read = input().strip()
    if read == '0':
        break
    if pal(read):
        print("yes")
    else:
        print("no")