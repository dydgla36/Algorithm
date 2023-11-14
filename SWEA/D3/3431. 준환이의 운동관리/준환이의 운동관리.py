for tc in range(1, int(input()) + 1):
    l, u, x = map(int, input().split())
    result = 0
    if x >= u:
        result = -1
    elif l >= x:
        result = l - x
    print(f'#{tc} {result}')
