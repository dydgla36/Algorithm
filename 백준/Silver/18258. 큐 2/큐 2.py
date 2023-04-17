import sys
from collections import deque
input = sys.stdin.readline

q = deque([])

# 명령의 수
N = int(input())

for i in range(N):
    x = list(input().split())
    if x[0] == 'push':
        q.append(int(x[1]))
    if x[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    if x[0] == 'size':
        print(len(q))
    if x[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    if x[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    if x[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])