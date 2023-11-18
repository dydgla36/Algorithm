for tc in range(1, int(input()) + 1):
    s, t = map(str, input().split())
    l_s = len(s)
    t_s = len(t)
    if s * t_s == t * l_s:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')

