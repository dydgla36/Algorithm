t = int(input())
for tc in range(1, t + 1):
    h1, m1, h2, m2 = map(int, input().split())
    m = m1 + m2
    h = h1 + h2
    if m >= 60:
        h = h + 1
        m = m - 60
    if h > 12:
        h = h - 12
    print(f'#{tc} {h} {m}')

