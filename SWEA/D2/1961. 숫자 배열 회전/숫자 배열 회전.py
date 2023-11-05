def degree_90(data):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = data[n - 1 - j][i]
    return result
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    data_90 = degree_90(data)
    data_180 = degree_90(data_90)
    data_270 = degree_90(data_180)

    print(f'#{tc}')
    for value_90, value_180, value_270 in zip(data_90, data_180, data_270):
        result_90 = ''.join(map(str, value_90))
        result_180 = ''.join(map(str, value_180))
        result_270 = ''.join(map(str, value_270))
        print(result_90, result_180, result_270)

# t = int(input())
# for tc in range(1, t + 1):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#
#     data_90 = [[0] * n for _ in range(n)]
#     data_180 = [[0] * n for _ in range(n)]
#     data_270 = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             data_90[i][j] = data[n - 1 - j][i]
#             data_180[i][j] = data[n - 1 - i][n - 1 - j]
#             data_270[i][j] = data[j][n - 1 - i]
#     print(f'#{tc}')
#     for value_90, value_180, value_270 in zip(data_90, data_180, data_270):
#         result_90 = ''.join(map(str, value_90))
#         result_180 = ''.join(map(str, value_180))
#         result_270 = ''.join(map(str, value_270))
#         print(result_90, result_180, result_270)