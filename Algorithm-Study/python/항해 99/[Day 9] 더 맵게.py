# 프로그래머스 더 맵게 https://school.programmers.co.kr/learn/courses/30/lessons/42626

'''
[📌 분석]
- 계속해서 작은 수를 찾아야 하기 때문에 힙을 이용

[✅ 풀이]
- 주어진 배열을 힙으로 변환
힙에 원소가 있을 때 반복
1. 힙에 원소가 1개보다 작거나 같고, 최소값이 K보다 작을 때는 스코빌 지수를 K 이상으로 만들 수 없기에 1 return
2. pop을 해서 가장 작은 원소 확인하고 K보다 크다면 최소 횟수 리턴
3. pop한 원소가 K보다 클 때에는 스코빌 지수 계산해 push, 최소 횟수 증가

'''

import heapq
from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
        popItem = heappop(scoville)
        if popItem >= int(K):
            return answer
        else:
            heappush(scoville, popItem + heappop(scoville) * 2)
            answer += 1