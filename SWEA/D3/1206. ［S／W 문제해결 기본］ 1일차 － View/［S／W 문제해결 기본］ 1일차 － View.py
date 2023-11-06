for tc in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n - 2):
        f1 = data[i] - data[i - 1]
        f2 = data[i] - data[i - 2]
        f3 = data[i] - data[i + 1]
        f4 = data[i] - data[i + 2]
        if f1 > 0 and f2 > 0 and f3 > 0 and f4 > 0:
            m = min(f1, f2, f3, f4)
            cnt += m
    print(f'#{tc} {cnt}')

