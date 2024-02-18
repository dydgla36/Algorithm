from collections import deque
import sys
input=sys.stdin.readline
cnt = 0
q = deque()
def rotate(n):
    global cnt, q
    cnt += abs(n)
    q = deque(list(q)[-n:] + list(q)[:-n])
n,m = map(int, input().split())
q = deque(i for i in range(1, n+1))
qry = list(map(int, input().split()))
for x in qry:
    if not q[0] == x: 
        idx = q.index(x)
        if idx <=  len(q) - idx: 
            rotate(-idx); 
        else: 
            rotate(len(q) - idx); 
    if q[0] == x: q.popleft()
print(cnt)
