# cnt = 0
# n = int(input())
# col = [0]*(n+1)

# def promising(i):
#     k = 1
#     while k < i:
#         if col[i] == col[k] or abs(col[i]-col[k]) == i-k:
#             return False
#         k += 1
#     return True
    
# def n_queens(i):
#     global cnt
#     if i == n:
#         cnt += 1
#     else:
#         for j in range(1, n+1):
#             col[i + 1] = j
#             if promising(i+1):
#                 n_queens(i+1)

# n_queens(0)
# print(cnt)


import sys
input = sys.stdin.readline

n = int(input())

pos = [0] * n          # 각 열에 배치한 퀸의 위치
flag_a = [False] * n   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * (n*2)  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * (n*2)  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크
# def put() -> None:
#     """퀸을 놓는 상황을 □와 ■로 출력"""
#     for j in range(n):
#         for i in range(n):
#             print('■' if pos[i] == j else '□', end='')
#         print()
#     print()
count = 0
def set(i: int) -> None:
    global count
    """i 열의 알맞은 위치에 퀸을 놓기"""
    for j in range(n):
        if(     not flag_a[j]           # j 행에 아직 퀸을 놓지 않았으면
            and not flag_b[i + j]       # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
            and not flag_c[i - j + n-1]): # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
            pos[i] = j          # 퀸을 j 행에 놓기
            if i == n-1:          # 모든 열에 퀸을 배치하는 것을 완료
                count += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + n-1] = True
                set(i + 1)      # 다음 열에 퀸을 놓기
                flag_a[j] = flag_b[i + j] = flag_c[i - j + n-1] = False

set(0)          # 0 열에 퀸을 놓기
print(count)