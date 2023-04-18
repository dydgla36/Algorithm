
# 최소한의 비교가 필요하므로 가장 작은 두 수의 합을 이용해 차례로 합치는 것이 가장 좋다
# m과 card의 리스트를 만들어 for문을 통해 card리스트를 받았다
# 만약 card값에 하나의 객체만 있으면 확인할 필요가 없기때문에 0번을 출력하고
# 다른 경우에는 sum로 결과값을 정하고 결과값에서 card에서 arr1과 arr2의 최소값을 빼준 값을
# sum에 더 해준다. 더 해준값을 다시 heappush로 card에 넣어주고 card의 길이가 0이 될때까지 반복함
import sys
input = sys.stdin.readline
import heapq
n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input())) 
     
if len(card) == 1:
    print(0)
    
else:
    sum = 0
    while len(card) > 1:
        arr1 = heapq.heappop(card)
        arr2 = heapq.heappop(card)
        sum += arr1 + arr2
        heapq.heappush(card, arr1 + arr2)
    print(sum)