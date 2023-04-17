import sys
input = sys.stdin.readline
from collections import deque

q = deque()
# 명령의 수
N, K = map(int, input().split())
list = []
for i in range(1, N+1):
    q.append(i)
count = 1
while q:
    if count % K == 0:
        list.append(q.popleft())
        count += 1
    else:
        q.append(q.popleft())
        count += 1
print("<",end= '')
for j in range(N-1):
    print(list[j],end=', ')
print(list[-1],end= '')
print(">")