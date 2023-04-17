import sys
input = sys.stdin.readline

N = int(input()) # 탑의 개수
top = list(map(int, input().split())) # 탑 리스트
stack = []
answer = []
for i in range(N):
    while stack:
        if stack[-1][1] > top[i]: # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack: # stack이 비면 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, top[i]]) # idx, value
for j in answer:
    print(j, end=' ')
    