# 프로그래머스 하노이의 탑 https://school.programmers.co.kr/learn/courses/30/lessons/12946
'''
[📌 분석]
- 재귀함수를 이용해 문제 풀이

[✅ 풀이]
재귀 조건
1. 원판이 한개일 경우 바로 left → right로 옮겨 함수를 종료합니다.
2. 원판이 한개보다 많을 경우 `n - 1` 개의 원판을 left → middle 옮김
3. 가장 큰 원판을 left → right 옮김
4. `n - 1` 개의 원판을 middle → right로 옮김

'''

hanoiList = []

def solution(n):
    hanoi(hanoiList, 1, 2, 3, n)
    return hanoiList


def hanoi(list, left, middle, right, n):
    if n == 1:
        tmpList = []
        tmpList.append(left)
        tmpList.append(right)
        list.append(tmpList)
    else:
        hanoi(list, left, right, middle, n - 1)
        hanoi(list, left, middle, right, 1)
        hanoi(list, middle, left, right, n - 1)
