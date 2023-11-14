for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b + 1):
        result = i ** (1 / 2)
        if result == int(result):
            i = str(i)
            result = str(int(result))
            if i == i[::-1] and result == result[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')