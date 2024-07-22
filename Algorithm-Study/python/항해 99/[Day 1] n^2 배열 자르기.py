# 프로그래머스 n^2 배열 자르기 https://school.programmers.co.kr/learn/courses/30/lessons/87390

'''
[📌 분석]
- 시간초과 발생 여부를 우려해 주어진 범위 안에서의 값을 구하는 것이 포인트

[✅ 풀이]
- 주어지는 2차원 배열에 값을 모두 넣어 생성하는 방식은, n 범위에 따라 값을 넣기만 해도 시간초과가 발생한다는 사실을 알게 되었고 
- 주어진 범위에 따라 그 부분만 반환할 수 있도록 구현했습니다.
- 현재 배열 인덱스 값을 n으로 나눈 나머지와, n으로 나눈 값 중에서 더 큰 값을 배열에 넣어 반환해주었습니다.

'''

def solution(n, left, right):

    arr = []
    count = right - left + 1
    for _ in range(count):
        tmp = left // n + 1
        tmp2 = left % n + 1
        arr.append(max(tmp, tmp2))
        left += 1
    return arr