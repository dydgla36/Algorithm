def dfs(level, sum_sub):
    global cnt
    if level >= N:
        return
    if sum_sub + arr[level] == S:
        cnt += 1
    dfs(level + 1, sum_sub + arr[level]) #level번째 원소를 부분수열에 포함
    dfs(level + 1, sum_sub)              #level번쨰 원소를 부분수열에 미포함


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)

# from itertools import combinations

# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0

# for i in range(n):
#     subarr = combinations(arr, i+1)
#     for j in subarr:
#         if sum(j) == s:
#             cnt += 1
# print(cnt)
