# 프로그래머스 문자열 내 마음대로 정렬하기 https://school.programmers.co.kr/learn/courses/30/lessons/12915

'''
[📌 분석]
- 주어진 n번째 인덱스 값을 기준으로 정렬
- 인덱스 n의 문자가 같은 경우 사전순으로 앞선 문자열이 우선정렬

[✅ 풀이]
1. 사전순으로 정렬
2. 인덱스 n의 값을 기준으로 재정렬 (lambda 사용)

'''

def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: (x[n]))
    return strings