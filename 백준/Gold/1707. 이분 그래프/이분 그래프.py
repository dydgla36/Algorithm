import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 백준 재귀제한 해제

from collections import deque

tc = int(input())

# 변형한 dfs
def dfs(node,color):

    global answer
	
    # 방문 시 표시를 color로 표현 
    # visited리스트의 각 값은 -1,0,1 중 하나
    visited[node] = color
    for i in graph[node]:
        if visited[i] == 0 :
        # 방문하지 않았다면 -color를 주어 색을 바꿈
            dfs(i,-color)
        elif visited[i] == -color:
            pass
        else:
            answer = "NO"
            return

def bfs(node, color):
    global answer
    
    queue = deque([(node, color)])
    visited[node] = color
    
    while queue:
        curr, curr_color = queue.popleft()
        
        for neighbor in graph[curr]:
            if visited[neighbor] == 0:
                visited[neighbor] = -curr_color
                queue.append((neighbor, -curr_color))
            elif visited[neighbor] == curr_color:
                answer = "NO"
                return

for _ in range(tc):
    V,E = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(V)]
    answer = "YES"
    for _ in range(E):
        u,v = map(int,sys.stdin.readline().split())

        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    visited = [0] * V

    for i in range(V):
        if visited[i] == 0 : 
            bfs(i,1)

    print(answer)