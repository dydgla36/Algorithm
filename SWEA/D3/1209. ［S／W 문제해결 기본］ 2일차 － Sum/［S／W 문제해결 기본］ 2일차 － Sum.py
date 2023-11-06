for tc in range(1, 11):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    max_value = row_value = col_value = cross_value = 0
    for i in range(100):
        row_value = 0
        for j in range(100):
            row_value += data[i][j]
        if row_value > max_value:
            max_value = row_value
    for i in range(100):
        col_value = 0
        for j in range(100):
            col_value += data[j][i]
        if col_value > max_value:
            max_value = col_value
    for i in range(100):
        cross_value += data[i][i]
        if cross_value > max_value:
            max_value = cross_value
    cross_value = 0
    for i in range(99, -1, -1):
        cross_value += data[i][99-i]
        if cross_value > max_value:
            max_value = cross_value

    print(f'#{tc} {max_value}')