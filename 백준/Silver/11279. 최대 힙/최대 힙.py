#최대힙
import sys
input = sys.stdin.readline
import heapq
q = []

n = int(input())
for i in range(n) :
    x = int(input())
    if x == 0 :
        if len(q) == 0 :
            print(0)
        else :
            print(heapq.heappop(q)[1])
    else :
        heapq.heappush(q, (-x, x))
        
#최소힙
# import sys
# input = sys.stdin.readline
# import heapq
# q = []

# n = int(input())
# for i in range(n) :
#     x = int(input())
#     if x == 0 :
#         if len(q) == 0 :
#             print(0)
#         else :
#             print(heapq.heappop(q))
#     else :
#         heapq.heappush(q, x)

