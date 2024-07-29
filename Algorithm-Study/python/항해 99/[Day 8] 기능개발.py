# 프로그래머스 기능개발  https://school.programmers.co.kr/learn/courses/30/lessons/42586

'''
[📌 분석]
- 일단 리스트 두개가 주어지고, 그 리스트에 각각 인덱스 값을 더해가면서 맨 처음 값이 100보다 크거나 같을 때, pop을 해줍니다.
- pop 이후에는 tmp 변수의 값을 증가시키고, 100이 넘은 값은 모두 pop을 해줍니다 (while 반복문 사용)

[✅ 풀이]
1. 반복은 `progresses` 배열이 존재할 때
2. `progresses` 배열 맨 처음 인덱스 값이 100보다 크거나 같을 때 반복
    1. `progresses` 배열과 `speeds` 배열 모두 pop(0)
    2. `tmp` 증가
    3. 만약 `progresses` 배열이 모두 pop되어 존재하지 않으면 break
3. tmp가 0보다 클 때 배포가 이루어진 것이므로 `answer` 배열에 append 해준뒤 다시 tmp 초기화
4. 둘다 해당하지 않는다면 아직 작업 중이므로 계속해서 `progresses[i]` 에 `speeds[i]` 값 더해줌

'''

def solution(progresses, speeds):
    answer = []
    tmp = 0

    while progresses:
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            tmp += 1
            if not progresses:
                break
        if tmp > 0:
            answer.append(tmp)
            tmp = 0
        else:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
    return answer


'''
# 시간복잡도가 더 적은 코드
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
'''