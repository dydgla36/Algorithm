for tc in range(1, int(input()) + 1):
    n = int(input())
    nn = n // 2
    s = input()
    if s[:nn] == s[nn:]:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')