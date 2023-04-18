
# 왼쪽, 오른쪽 힙을 각각 만들어, 중간값을 기준으로 더 작은 값들은 왼쪽 힙에, 더 큰 값들은 오른쪽 힙에 넣는다는 아이디어이다.
# 여기서 중요한건, 각 힙의 가장 첫 번째 값, 즉 0번 인덱스 값은 해당 힙의 가장 우선순위가 높은 값이라는 것이다.
# heapq 라이브러리를 사용해 만든 힙은 기본적으로 최소힙을 구성하고 있으며, 힙에 push되는 값을 음수로 만들어주는 방식으로 최대힙도 만들 수 있다.
# 중간값보다 작은 값들이 저장되는 왼쪽 힙은 최대힙으로, 큰 값들이 저장되는 오른쪽 힙은 최소힙으로 만들어주게 되면,
# 왼쪽 힙은 pop할 때마다 중간값보다 작은 값들 중 가장 큰 값들부터 힙을 빠져나올 것이고
# 오른쪽 힙은 pop할 때마다 중간값보다 큰 값들 중 가장 작은 값들부터 힙을 빠져나올 것이다.
# 그리고 만약에 왼쪽 힙 중 가장 우선순위가 높은 값 즉, 가장 큰 값이 오른쪽 힙의 가장 우선순위가 높은 값인 가장 작은 값보다 클 경우, 두 수를 바꿔주면 중간값을 기준으로 숫자들을 쭉 나눠놓을 수 있다.
# 예를 들어서, 왼쪽 힙에 담긴 값들이 [1, 2, 7]이고, 오른쪽 힙에 담긴 값들이 [3, 8, 9]일 때, 
# 왼쪽 힙의 가장 우선순위가 높은 값을 7이 될 것이고, 오른쪽 힙의 가장 우선순위가 높은 값은 3이될 것이다.
# 따라서, 두 숫자를 바꿔주는 작업을 실행하면 [1, 2, 3]과 [7, 8, 9]로, 중간값(3 or 7)을 기준으로 input값들이 나눠진 것을 확인할 수 있다.
import sys
input = sys.stdin.readline
import heapq
n = int(input())
left_heap = []
right_heap = []

for _ in range(n):
    x = int(input())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)   #중간값 출력하기 위해서 -를 변수앞에 붙임
    
    else:
        heapq.heappush(right_heap, x)
        
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value * -1)

    print(left_heap[0] * -1)