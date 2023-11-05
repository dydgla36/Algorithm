t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    m = list(map(int, input().split()))
    m.sort()
    print(f'#{tc}', end = ' ')
    print(*m)
