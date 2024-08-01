# 프로그래머스 카드 뭉치 https://school.programmers.co.kr/learn/courses/30/lessons/159994
'''
[📌 분석]
- goal 배열에 있는 값을 카드 배열들과 하나씩 비교

[✅ 풀이]
- 카드 배열 두개에 다 값이 있는지 확인 이후에 값을 비교해 pop을 해주었습니다.

'''

def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.pop(0)
        elif cards2 and word == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'