# import itertools

# N = int(input())

# input_array = list(map(int, input().split()))
# result = 0 #결과 값을 저장할 result 값 선언


# def result_solve(array):  # 리스트의 차를 구하는 공식
#     global result

#     def_result = 0 #각 원소의 차를 저장
#     for i in range(len(array) - 1):
#         def_result += abs(array[i] - array[i + 1]) #각 원소의 차의 절대값을 계속해서 더해나간다.
#     result = max(result, def_result) #저장되어있는 결과값과 비교해서 큰 값을 결과값에 대입


# for i in itertools.permutations(input_array, N): #permutations라이브러리 이용(입력받은 리스트의 원소중에서 N개를 뽑는다.)
#     result_solve(i) #뽑은 순열마다 리스트의 차를 구하여 result에 대입

# print(result)
# import itertools
# import sys

# sys.setrecursionlimit(100001)
# N = int(input())

# input_array = list(map(int, input().split()))
# result = 0  # 각 리스트 원소의 차의 최대값을 저장할 result
# input_array.sort()  # 처음부터 끝까지 리스트의 모든 순열을 뽑기 위해 오름차순으로 정열
# result_array = sorted(input_array, reverse=True)  # 재귀 탈출을 위해 마지막 순번인 내림차순으로 정렬후 새로운 리스트에 대입

# def result_solve(array):  # 리스트의 차를 구하는 공식
#     global result

#     def_result = 0 #각 원소의 차를 저장
#     for i in range(len(array) - 1):
#         def_result += abs(array[i] - array[i + 1]) #각 원소의 차의 절대값을 계속해서 더해나간다.
#     result = max(result, def_result) #저장되어있는 결과값과 비교해서 큰 값을 결과값에 대입

# def all_permutations_solve(def_array):
#     global result

#     result_solve(def_array) #리스트의 차를 구하는 공식에 모든 순열을 순차적으로 대입
#     # 리스트 출력
#     if def_array == result_array:  # 만약 재귀를 돌면서 나온 순열이 나올 수 있는 모든순열의 마지막 순열이라면
#         print(result)  # result값출력
#         exit()  # 코드 종료

#     for i in range(N - 1, 0, -1):  # 마지막 항부터 돈다
#         if def_array[i - 1] < def_array[i]:  # 만약 앞 열의 값이 그 뒷열의 값보다 작다면
#             for j in range(N - 1, 0, -1):  # 다시 그 앞 열의 값을 맨 뒷열부터 비교
#                 if def_array[i - 1] < def_array[j]:  # 그 앞열의 값이 뒤에 있는 어느 열보다 작다면
#                     def_array[i - 1], def_array[j] = def_array[j], def_array[i - 1]  # 그 두 값을 스왑
#                     def_array = def_array[:i] + sorted(def_array[i:])  # i-1 번째 까지의 리스트와 그 뒤에리스트를 정렬한 채로 붙인다.
#                     all_permutations_solve(def_array)  # 이 과정을 반복
# all_permutations_solve(input_array)

def check(depth):   
    if len(M)==N:                   #M의 길이가 N과 같으면
        global total                #전역변수 total 설정
        sum=0                       #sum에 0으로 초기화
        for i in range(N-1):        
            sum+=abs(M[i]-M[i+1])   
        total=max(sum,total)
        return
    for i in range(N): 
        if not visited[i]:
            visited[i]=True
            M.append(l[i])
            check(depth+1)
            M.pop()
            visited[i]=False

N=int(input())
l=list(map(int,input().split()))
visited=[False]*N   #N의 배열만큼 증가시켜서 False값을 저장
M=[]    #배열 지정
total=0

check(0)    #dfs방식 

print(total)

# 모든 수열 찾을 때 사용하는 코드
# def check(depth):
#     if len(M)==N:
#         answer.append(str(M))
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i]=True
#             M.append(l[i])
#             check(depth+1)
#             M.pop()
#             visited[i]=False

# N=int(input())
# l=list(map(int,input().split()))
# visited=[False]*N
# M=[]
# answer=[]

# check(0)

# print(answer)