# 프로그래머스 전화번호 목록 https://school.programmers.co.kr/learn/courses/30/lessons/42577

'''
[📌 분석]
- 번호가 포함되는지 확인하기 위해 정렬 필요

[✅ 풀이]
- startswith를 이용해 문자열이 포함되어 있는지 빠르게 파악

'''

def solution(phone_book):
    phone_book.sort()
    
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i - 1]):
                return False
    return True