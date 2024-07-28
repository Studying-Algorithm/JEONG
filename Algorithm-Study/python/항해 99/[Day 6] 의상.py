# 프로그래머스 의상 https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''
[📌 분석]
- 딕셔너리를 사용해 의상을 분류하고, 경우의 수를 토대로 값 리턴

[✅ 풀이]
- 딕셔너리를 만들어 Key 값이 존재하는지 확인한 이후, 
만약 값이 있다면 value를 증가시켜 주고 없다면 1로 초기화를 해 옷을 분류했다
- 딕셔너리를 만들어 Key 값이 존재하는지 확인한 이후, 
만약 값이 있다면 value를 증가시켜 주고 없다면 1로 초기화를 해 옷을 분류했다

'''

def solution(clothes):
    dict = {}
    result = 1

    for _, cloth in clothes:
        if cloth in dict:
            dict[cloth] += 1
        else:
            dict[cloth] = 1

    for count in dict.values():
        result *= count + 1
    return result - 1
