import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque

T = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    XY[x][y] = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < M and 0 <= new_y < N and XY[new_x][new_y] > 0:
            if XY[new_x][new_y] == 1:
                XY[new_x][new_y] = 0
                dfs(new_x,new_y)

# queue = deque()
# def bfs(x, y):
#     queue.append((x,y))
#     XY[x][y] = 0
#     while queue:
#         p, q = queue.popleft()
#         for i in range(4):
#             new_x = p + dx[i]
#             new_y = q + dy[i]
            
#             if 0 <= new_x < M and 0 <= new_y < N and XY[new_x][new_y] > 0:
#                 if XY[new_x][new_y] == 1:
#                     queue.append((new_x, new_y))
#                     XY[new_x][new_y] = 0
for i in range(T):
    M, N, K = map(int, input().split())
    XY = [[0] * N for _ in range(M)]
    count = 0
    
    for l in range(K):
        x, y = map(int, input().split())
        XY[x][y] = 1
    
    for j in range(M):
        for k in range(N):
            if XY[j][k] == 1:
                dfs(j,k)
                # bfs(j,k)
                count += 1
    print(count)