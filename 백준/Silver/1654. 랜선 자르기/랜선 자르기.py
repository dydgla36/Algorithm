import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start, end = 1, max(lan) #이분탐색 처음과 끝위치

while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중간 위치
    count = 0 #랜선 수
    for i in lan:
        count += i // mid #분할 된 랜선 수
    if count >= N: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)
