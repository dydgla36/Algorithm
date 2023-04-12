from collections import deque
 
n = int(input())
max_num = 0
graph = []
 
for _ in range(n):          # 입력한 값중에 제일 큰값을 찾음
    low = list(map(int, input().split()))
    graph.append(low)
 
    for i in low:
        if i > max_num:
            max_num = i
 
dx = [0, 0, -1, 1]  # x좌표 기준
dy = [1, -1, 0, 0]  # y좌표 기준
 
def bfs(x, y, num):
    queue = deque() # 큐 = deque[root] 큐를 생성
    queue.append((x, y))    #큐에 x,y 좌표 추가
    visited[x][y] = 1       #위에 좌표를 갔으면 방문기록 남김
 
    while queue:            
        q_x, q_y = queue.popleft()  #queue의 맨 왼쪽 요소를 뽑아서  x, y에 저장
 
        for i in range(4):          #어디로 이동했는지 확인 작업 ↑↓←→ 순서로 찾음
            nx = dx[i] + q_x        # 예를 들어 0,0 이면 i가 0일 때 0의 값을 nx에 넣음
            ny = dy[i] + q_y        # 예를 들어 0,0 이면 i가 0일 때 1의 값을 ny에 넣음
 
            if 0 <= nx < n and 0 <= ny < n:                         # nx, ny가 안전영역인지 확인(인덱스 범위안에 있는지)
                if graph[nx][ny] > num and visited[nx][ny] == 0:    # 탐색 위치의 값이 입력한 값보다 크고 방문한적 없으면
                    visited[nx][ny] = 1                             # 방문한적 있다고 표시

                    queue.append((nx, ny))                          #nx,ny값을 큐에 추가
 
result = [] # result 배열 사용
for i in range(max_num):                                
    cnt = 0
    visited = [[0]*n for _ in range(n)]                 # visited 크기를 graph 크기만큼 증가
    for j in range(n):                                  
        for k in range(n):                              
            if graph[j][k] > i and visited[j][k] == 0:  #굳이 방문하거나 높이가 작은 것들은 bfs를 할 필요 없어서
                bfs(j, k, i)                           
                cnt += 1                                #다시 돌아와 여기오게 되면 인근에 안전영역이 없기 때문에 하나의 영역으로 생각하고 갯수 증가
    result.append(cnt)
 
print(max(result))