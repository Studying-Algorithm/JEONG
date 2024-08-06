# 프로그래머스 모음사전 https://school.programmers.co.kr/learn/courses/30/lessons/84512
'''
[📌 분석]
- 중복 순열을 만들어 인덱스 찾기

[✅ 풀이]
- prodcut 함수 사용

'''

from itertools import product

def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    list = []

    for len in range(1, 6):
        for i in product(alphabets, repeat=len):
            list.append(''.join(i))
    list.sort()
    return list.index(word) + 1