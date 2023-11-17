for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    if a == b:
        result = a
    else:
        result = 1
    print(f'#{tc} {result}')