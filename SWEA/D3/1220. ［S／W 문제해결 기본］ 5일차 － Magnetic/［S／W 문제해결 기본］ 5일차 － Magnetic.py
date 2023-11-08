for tc in range(1, 11):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        state = 0
        for j in range(n):
            if data[j][i] == 1 and state == 0:
                state = 1
            elif data[j][i] == 2 and state == 1:
                state = 0
                cnt += 1
    print(f'#{tc} {cnt}')