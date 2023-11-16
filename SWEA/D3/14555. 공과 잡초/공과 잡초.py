for tc in range(1, int(input()) + 1):
    s = input()
    cnt = 0

    cnt += s.count('()')
    cnt += s.count('(|')
    cnt += s.count('|)')

    print(f'#{tc} {cnt}')
