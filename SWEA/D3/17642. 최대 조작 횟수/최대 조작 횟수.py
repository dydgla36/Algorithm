for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    c = b - a
    if c == 0:
        cnt = 0
    elif c <= 1:
        cnt = -1
    elif c % 2 == 0:
        cnt = c // 2
    else:
        cnt = (c - 3) // 2 + 1
    print(f'#{tc} {cnt}')