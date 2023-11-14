for tc in range(1, int(input()) + 1):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    p, q = n // 2, n // 2
    result = 0
    for i in range(n):
        for j in range(p, q + 1):
            result += data[i][j]
        if i < n // 2:
            p -= 1
            q += 1
        else:
            p += 1
            q -= 1
    print(f'#{tc} {result}')