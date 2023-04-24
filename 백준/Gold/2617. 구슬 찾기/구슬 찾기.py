import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

from collections import defaultdict
from collections import deque


N, M = map(int, input().split())
heavier = defaultdict(list)
lighter = defaultdict(list)
answer = 0
visited = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    heavier[B].append(A)
    lighter[A].append(B)

def heavier_dfs(x):
    visited[x] = 1
    for i in heavier[x]:
        if not visited[i]:
            heavier_dfs(i)
            
def heavier_bfs(x):
    visited[x] = 1
    queue = deque([x])
    while queue:
        node = queue.popleft()
        for i in heavier[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
  
def lighter_dfs(x):
    visited[x] = 1
    for i in lighter[x]:
        if not visited[i]:
            lighter_dfs(i)
            
def lighter_bfs(x):
    visited[x] = 1
    queue = deque([x])
    while queue:
        node = queue.popleft()
        for i in lighter[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

for j in list(heavier):
    visited = [0] * (N + 1)
    heavier_dfs(j)
    # heavier_bfs(j)
    if(visited.count(1)-1 >= (N+1)//2):
        answer += 1

for k in list(lighter):
    visited = [0] * (N + 1)
    lighter_dfs(k)
    # lighter_bfs(k)
    if(visited.count(1)-1 >= (N+1)//2):
        answer += 1
        
print(answer)


