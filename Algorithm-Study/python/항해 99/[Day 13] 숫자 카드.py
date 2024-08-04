# 백준 10815 숫자 카드 https://www.acmicpc.net/problem/10815
'''
[📌 분석]
- 이진 탐색을 이용한 풀이

[✅ 풀이]
- bisect 모듈을 사용해 풀 수 있었다.
- bisect 명령어가 오름차순된 배열에서 알맞은 인덱스 위치를 찾아준다는 것을 이용
- index의 왼쪽 값이(index - 1) 찾는 값과 동일하다면 배열에 존재한다는 것을 알 수 있었다.

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
    for i in numCards:
        if cards[bisect.bisect(cards, i) - 1] == i:
            result.append(1)
        else:
            result.append(0)
    return result

print(*binarySearchCard(cards, numCards))