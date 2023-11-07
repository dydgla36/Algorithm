for tc in range(1, 11):
    n = int(input())
    data = [list(map(str, input())) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8 - n + 1):
            if data[i][j:j+n] == data[i][j:j+n][::-1]:
                cnt += 1
    for i in range(8 - n + 1):
        for j in range(8):
            if [data[k][j] for k in range(i, i+n)] == [data[k][j] for k in range(i, i+n)][::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')
