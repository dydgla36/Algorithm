import sys
input = sys.stdin.readline
from collections import deque

N = int(input())                #컴퓨터의 수 입력받기
link = int(input())             #네트워크 연결 컴퓨터 수 받기
visited = [0] * (N + 1)         #네트워크 방문 표시 길이를 컴퓨터 수만큼 받기

network = [[] * (N + 1) for _ in range(N + 1)]  # 네트워크를 2차원배열로 받을 수 있게 만들어 놓고
for i in range(link):                           # for문을 네트워크 연결 컴퓨터 수만큼 돌려
    a, b = map(int, input().split())            # 네트워크 연결 정보를 입력하고
    network[a].append(b)                        #network = [[],[2],[1]] 이런식으로 받을 수 있게
    network[b].append(a)


def bfs(target):
    cnt = 0                     #바이러스 걸린 컴퓨터 수를 받을 수 있게
    queue = deque()             #큐를 생성한다 
    queue.append(target)        #큐에 타켓을 추가한다
    visited[target] = 1         #처음으로 들어왔으니깐 visited[target]를 1로 주어 방문 기록 남김
    while queue:                #큐에 값이 있으면
        x = queue.popleft()     #x = queue.popleft를 해서 맨 왼쪽 요소를 빼서 x에 저장하고
        for i in network[x]:    #for문을 돌려 network[x]을 i에 넣으면서  
            if visited[i] == 0: #만약 방문기록이 없으면 방문기록을 남기고 cnt를 1 증가시키고 큐에 i값을 추가한다.
                visited[i] = 1  
                cnt +=1
                queue.append(i)
                
    return cnt

print(bfs(1))
    