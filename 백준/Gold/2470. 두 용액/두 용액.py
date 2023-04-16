# 1. 이 코드는 N개의 용액을 입력 받고, 이 중에서 두 개의 용액을 혼합하여 특성값이 0에 가까운 용액을 만들려고 합니다.
# 2. 이를 위해서는 용액의 특성값이 가장 작은 용액과 가장 큰 용액을 혼합하면 되는 것이 아니라, 특성값이 0에 가까운 두 용액을 혼합해야 합니다. 
# 3. 이 문제에서는 두 용액의 합의 절대값이 가장 작은 두 용액을 찾으면 되므로, 이분 탐색을 이용하여 해결할 수 있습니다.
# 4. 먼저, 입력 받은 N개의 용액을 오름차순으로 정렬합니다. 그리고 f_solution() 함수에서는 이분 탐색을 이용하여 특성값이 0에 가까운 두 용액을 찾습니다. 
# 5. 이를 위해서는 모든 용액에 대해서 이분 탐색을 수행해야 하므로 N번 반복문을 수행합니다. 
# 6. 이 중에서 i번째 용액을 기준으로 생각하여, i+1번째 용액부터 N번째 용액까지 이분 탐색을 수행합니다.
# 7. 이분 탐색에서는 찾는 값이 (현재 용액 * -1)이므로, 이분 탐색을 수행하면서 현재 용액의 반대값에 해당하는 용액을 찾습니다. 
# 8. 이를 위해서는 이분 탐색을 수행하면서 현재 용액의 반대값에 해당하는 용액을 찾으면, 그보다 왼쪽에 있는 용액들은 이미 확인한 용액이므로 더 이상 탐색할 필요가 없습니다.
# 9. 찾은 두 용액의 합의 절대값이 이전에 찾은 두 용액의 합의 절대값보다 작으면, 이 두 용액을 선택합니다. 최종적으로 선택된 두 용액의 특성값을 출력합니다.

import sys
input = sys.stdin.readline

n = int(input())
solution = sorted(map(int, input().split()))  # 용액들을 입력 받아서 오름차순으로 정렬한다

def binary_search(s, target):   #이진 탐색
    global solution
    res = n
    start, end = s, n - 1

    while start <= end:
        mid = (start + end) // 2
        if solution[mid] >= target:
            res = mid
            end = mid - 1
        else: 
            start = mid + 1
    return res


def f_solution():   #용액의 특성값이 0에 가까운 용액 만드는 작업
    global solution
    v1, v2 = 0, 0
    best_sum = 10 ** 10
    for i in range(n):
        # 이분 탐색 수행: 현재 위치(i) 이후의 용액에서 탐색, 찾는 값은 (현재 용액 * -1)
        res = binary_search(i + 1, -solution[i])
        
        # 찾은 용액의 왼쪽 용액 확인 
        
        if i + 1 <= res - 1 < n and abs(solution[i] + solution[res - 1]) < best_sum:
            best_sum = abs(solution[i] + solution[res - 1])
            v1, v2 = solution[i], solution[res - 1]

        # 찾은 용액 확인
        if i + 1 <= res < n and abs(solution[i] + solution[res]) < best_sum:
            best_sum = abs(solution[i] + solution[res])
            v1, v2 = solution[i], solution[res]
    
    print(v1, v2) # i 번째 용액을 확인할 때 i + 1번 용액부터 확인하기 때문에 항상 v1 <= v2 이다.

f_solution()