import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]     #2차원 배열 만듬
visited = [0]* n        #방문기록을 n만큼 배열로 만들어 0을 넣어줌
sum_cost = 0            # 모든 비용
ans = 100000001
# 0 → 1 → 2 → 3 이면 순서를 1 → 2 → 3 → 0 이런식으로 바꿔도 순서는 같아서 비용이 같음
def dfs(depth, x):
    global sum_cost, ans                        # sum_cost, ans 전역변수 설정
    if depth == n-1:                            # depth 
        if costs[x][0]:                         # 9라인 설명 처럼 같으니깐 0의 값을 고정해서 다른 숫자들을 바꿈
            sum_cost += costs[x][0]             # 다시 돌아가는 비용을 추가하기 위해서 넣어줌
            if sum_cost < ans:                  # 최소 비용을 찾기 위한 if문
                ans = sum_cost                  # ans 에 모든 비용을 구한 sum_cost의 값을 넣어줌
            sum_cost -= costs[x][0]             # 리턴을 할 때 sum_cost의 값을 이전에 값으로 만들어 주기위해 costs의 값을 빼줌
        return
    for i in range(1, n):                       
        if visited[i] == 0 and costs[x][i]:     # 방문기록이 없고 costs 값이 있으면 if문 동작
            visited[i] = 1                      # 방문 기록
            sum_cost += costs[x][i]             # sum_cost에 costs값을 추가해줌 
            dfs(depth+1, i)                     # depth+1해서 i와 같이 dfs 함수를 실행
            visited[i] = 0                      # return을 받고나면 for문을 끝내지 못해서 여기서부터 끝까지 실행
            sum_cost -= costs[x][i]             # sum_cost의 값을 이전에 값으로 만들어 주기위해 costs의 값을 빼줌

dfs(0, 0)       #처음에 0,0을 넣어서 실행함

print(ans)