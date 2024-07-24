# 백준 2504 괄호의 값 https://www.acmicpc.net/problem/2504

'''
[📌 분석]
1. (), []는 쌍이 항상 맞아야 한다. 맞지 않는다면 0 출력
2. ( 와 [ 다음 쌍이 맞지 않는다면 곱해지게 된다 )와 ]가 나오기 전까지
3. 바로 뒤에 )와 ]가 나오면 더하기가 된다
4. 계속 반복하게 된다

- 더하기 구현을 어떻게 해야 하는지?
- 쌍이 맞지 않는 경우도 고려 ex. )(
- temp를 사용해 가중치를 곱하거나 더해줌

[✅ 풀이]
- temp 변수를 이용해 가중치를 부여했습니다.
- (와 [가 나왔을 시 가중치에 값을 곱해주고, 만약 스택이 비어있거나 괄호의 값이 일치하지 않는다면 종료
- 만약 짝을 찾았을 시에는 result에 현재 가중치를 더해준 이후 stack에서 pop, 그리고 가중치도 제거해줍니다.
- 만약 반복문이 종료되었는데 stack에 남아있는 괄호가 있을 경우 짝이 맞지 않는 경우이므로 0 리턴
'''


import sys

input = sys.stdin.readline

brackets = input().strip()
stack = []
result = 0
temp = 1

for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
        temp *= 2
    elif brackets[i] == '[':
        stack.append('[')
        temp *= 3
    elif brackets[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if brackets[i-1] == '(':
            result += temp
        stack.pop()
        temp //= 2

    elif brackets[i] == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if brackets[i - 1] == '[':
            result += temp
        stack.pop()
        temp //= 3

if stack:
    result = 0

print(result)