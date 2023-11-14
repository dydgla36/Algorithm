for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    result = -1
    if a < 10 and b < 10:
        result = a * b
    print(f'#{tc} {result}')