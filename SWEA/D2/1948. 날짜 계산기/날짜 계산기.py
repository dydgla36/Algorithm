date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for test_case in range(1, T + 1):
    m, d, n_m, n_d = map(int, input().split())
    result = 0
    if m == n_m:
        result = n_d - d + 1
    else:
        result = date[m - 1] - d + 1
        for i in range(m + 1, n_m):
            result += date[i - 1]
        result += n_d
    print(f'#{test_case} {result}')
        