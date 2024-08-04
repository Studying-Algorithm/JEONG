# 백준 10816 숫자 카드 2 https://www.acmicpc.net/status?user_id=kj9470&problem_id=10816&from_mine=1
'''
[📌 분석]
- 이진 탐색을 이용한 풀이

[✅ 풀이]
- bisect의 bisect_left와 bisect_right를 이용해서 같은 값이 있는지 파악하고 이를 append
- index 초과 에러가 발생해서 이에 대한 예외처리를 잘 확인해야 했다.

'''

import sys
import bisect

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
numCards = list(map(int, input().split()))

cards.sort()
def binarySearchCard(cards, numCards):
    result = []
    for n in numCards:
        idx = bisect.bisect(cards, n)
        if cards[idx - 1] == n:
            left_idx = bisect.bisect_left(cards, n)
            if left_idx + 1 < len(cards):
                if cards[left_idx + 1] == n:
                    result.append(idx - left_idx)
                else:
                    result.append(1)
            else:
                result.append(1)
        else:
            result.append(0)
    return result

print(*binarySearchCard(cards, numCards))