for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    result = 0
    if a + b >= 24:
        result = a + b - 24
    else:
        result = a + b
    print(f'#{tc} {result}')
