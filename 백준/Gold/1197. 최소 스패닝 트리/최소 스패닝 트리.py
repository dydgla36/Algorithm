#크루스칼 알고리즘
import sys
input = sys.stdin.readline  

v, e = map(int, input().split())    #정점의 개수, 간선의 개수
parent = [i for i in range(v+1)]    # 부모 id 만들어줌
edges = []                         
ans = 0                             # 최소 스패닝 트리의 가중치 출력

def find(parent, x):                # 노드를 연결하기 전에 두 노드가 같은 집합인지 검사하는 함수
    if parent[x] != x:              # 두 노드의 루트 노드를 찾아 비교함 같지 않다면
        parent[x] = find(parent,parent[x])  # 
    return parent[x]                

def union(parent, a, b):            # 두 노드를 연결 해주는 함수
    A = find(parent, a)             # find(parent, a)함수의 결과 값을 받아서 A에 저장
    B = find(parent, b)             # find(parent, b)함수의 결과 값을 받아서 B에 저장
    if A > B:                       # A 가 B보다 크다면
        parent[A] = B               # parent[A]에 B값 저장
    else:
        parent[B] = A               # parent[B]에 A값 저장

for i in range(e):
    a, b, c = map(int,input().split())  # a 정점, b 정점, c 가중치를 입력 받음
    edges.append((c,a,b))               # 입력 받은 값을 edges에 튜플 형식으로 저장
edges.sort()                            # edges의 c의 가중치를 기준으로 오름차순한다.

for edge in edges:                      # edges의 값을 순서대로 edge에 넣는 반복문
    cost, a, b = edge                   # edge의 튜플 형식의 값을 cost, a, b에 넣는다
    if find(parent, a) != find(parent, b):  # parent[a]의 값이 parent[b]의 값이랑 다르면
        union(parent, a, b)                 # 두 노드를 연결해주는 함수를 사용하여 연결해준다
        ans += cost                         # ans에 두 노드의 가중치 값을 넣는다    
print(ans)                                      

# # 프림 알고리즘
# import heapq
# import sys
# input = sys.stdin.readline

# V, E = map(int, input().split())
# visited = [False] * (V + 1)         # 방문한 정점 표시 하기 위해 생성
# graph = [[] for _ in range(V + 1)]  # 간선 정보를 저장하기 위해서 생성
# q = [(0, 1)]                        # 가중치가 가장 작은 간선정보를 저장하기위해 만듬(튜플형태로 간선 가중치, 끝점)을 저장
# for _ in range(E):       #간선의 정보 저장
#     A, B, C = map(int, input().split())     
#     graph[A].append((C, B))                 
#     graph[B].append((C, A))     

# cnt = 0                 # 방문한 정점 개수 저장
# ans = 0                 # 최소 스패닝 트리의 가중치 출력
# while q:                #q에 값이 계속 실행
#     if cnt == V:        # cnt의 방문한 정점의 개수와 V의 처음에 입력한 정점의 개수가 같으면
#         break           # 멈춤
#     cost, now = heapq.heappop(q)    #q의 값을 빼서 cost, now에 저장
#     if not visited[now]:            # visited[now] = False이면
#         visited[now] = True         # visited[now] = Ture로 바꿔주고
#         ans += cost                 # ans 에 가중치 cost를 더해주고
#         cnt += 1                    # 방문한 정점 개수 추가
#         for next in graph[now]:     
#             heapq.heappush(q, (next[0], next[1]))   #q에 next[0], next[1] 값을 넣어준다
# print(ans)