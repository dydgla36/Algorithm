import sys
input = sys.stdin.readline

# combinations함수사용
from itertools import combinations
n,m = map(int, input().split())
card = list(map(int, input().split()))
ans = 0
for i in combinations(card, 3):
    if ans < sum(i) <= m:
        ans = sum(i)
print(ans)

# 완전탐색
# n,m = map(int,input().split())

# card = list(map(int,input().split()))
# ans = 0
# for i in range(0,n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1,n):
#             sum = card[i] + card[j] + card[k]
#             if sum > m:
#                 continue
#             else:
#                 ans = max(ans, sum)
                
# print(ans)