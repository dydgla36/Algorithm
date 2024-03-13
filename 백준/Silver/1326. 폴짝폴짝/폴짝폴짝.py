from collections import deque
n = int(input())
bridge = [0] + list(map(int, input().split()))
start, end = map(int, input().split())
def bfs(s, e):
    q = deque([s])
    visited = [-1] * (n + 1)
    visited[s] = 0
    while q:
        now = q.popleft()
        for i in range(now, n + 1, bridge[now]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] + 1
                if i == e:
                    return visited[i]
        for i in range(now, 0, -bridge[now]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] + 1
                if i == e:
                    return visited[i]
    return -1 
print(bfs(start, end))