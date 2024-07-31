# 프로그래머스 이중우션큐 https://school.programmers.co.kr/learn/courses/30/lessons/42628
'''
[📌 분석]
- 최소 힙 모듈을 사용해 문제 해결

[✅ 풀이]
- 최솟값일 때는 heappop
- 최댓값일 때는 정렬 이후 pop
- 힙은 값이 없을 때 heappop을 하면 에러가 나기 때문에 항상 원소 존재 여부 확인

'''

import heapq
from heapq import heappop, heappush

def solution(operations):
    heap = []

    for operation in operations:
        alp, number = operation.split()
        number = int(number)
        if alp == 'I':
            heapq.heappush(heap, number)
        elif alp == 'D':
            if number == 1 and heap:
                heap.sort()
                heap.pop()
            elif number == -1 and heap:
                heapq.heappop(heap)

    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]