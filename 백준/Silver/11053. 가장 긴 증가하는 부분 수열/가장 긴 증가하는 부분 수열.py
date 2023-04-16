import sys
input = sys.stdin.readline

#이진 탐색
#n보다 작은 숫자들 중 최대값의 다음 칸에 위치시킨다.
def lower_bound(n): 
    l,r = 0,answer_len
    while l<=r:
        mid = (l+r)//2
        if answer[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
            save = mid
    answer[save] = n    

N=int(input())
num=list(map(int,input().split()))

answer = [num[0]]           # num리스트의 처음값을 answer에 추가
5
answer_len=1         
for i in num[1:]:           # num리스트의 1번 인덱스부터 끝까지 i에 넣어줌 
    if i > answer[-1]:      # i의 값이 answer 마지막 인덱스 값보다 크면
        answer.append(i)    # answer의 리스트 마지막에 i의 값을 추가함
        answer_len += 1     # answer_len 1 증가 (가장 긴 증가하는 부분 수열 구하는 변수)
    elif i < answer[-1]:    # i의 값이 answer 마지막 인덱스 값보다 작으면
    	lower_bound(i)      # lower_bound(n) 함수의 n에 i 값을 넣어줌

print(answer_len)

# DP
# import sys
# input = sys.stdin.readline

# n=int(input())
# value=list(map(int,input().split()))

# dp=list(0 for _ in range(n))
# dp[0]=1

# for i in range(1,n):
#     for j in range(i):
#     	#value[i]보다 값이 작은 숫자들의 dp값들 중 최대값을 dp[i]에 저장
#         if value[j]<value[i] and dp[j]>dp[i]:
#             dp[i]=dp[j]
#     dp[i]+=1

# print(max(dp))