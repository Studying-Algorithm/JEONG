# 프로그래머스 JadenCase 문자열 만들기 https://school.programmers.co.kr/learn/courses/30/lessons/12951#

'''
[📌 분석]
- 문자열을 나눠 배열에 저장해 맨 앞 문자만 upper()을 사용

[✅ 풀이]
- 공백을 제거하면 안되기 때문에 split을 할 때 주의

'''

def solution(s):
    arr = []
    answer = []
    
    s = s.lower()
    arr = s.split(" ")

    for word in arr:
        if word:
            if word[0].islower():
                word = word[0].upper() + word[1:]
        
        answer.append(word)
    
    answer = " ".join(answer)
        
    return answer

# capitalize() 함수를 이용한 풀이
'''
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])
'''