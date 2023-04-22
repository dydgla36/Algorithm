import sys
from collections import deque
sys.setrecursionlimit(5000)
input = sys.stdin.readline

N,M = map(int,input().split())

result = 0
graph = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    u, v = map(int,input().split())
    graph[u][v] = 1
    graph[v][u] = 1

visited = [0] * (N+1)

def dfs(v):
    visited[v] = 1
    for i in range(1,N+1):
        if not visited[i] and graph[v][i]:
            dfs(i)
            
def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in range(N+1):
            if not visited[i] and graph[v][i]:
                q.append(i)
                visited[i] = 1

for i in range(1, N+1):
    if not visited[i]:
        # bfs(i)
        dfs(i)
        result += 1

print(result)