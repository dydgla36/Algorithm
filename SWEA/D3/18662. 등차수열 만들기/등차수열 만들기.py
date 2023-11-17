for tc in range(1, int(input()) + 1):
    a, b, c = map(int, input().split())
    d = b - a
    e = c - b
    if d == e:
        print(f'#{tc} 0.0')
    else:
        print(f'#{tc} {abs(d - e) / 2}')