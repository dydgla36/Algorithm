for tc in range(1, int(input()) + 1):
    n = list(map(int, input().split()))
    if n[0] == n[1]:
        print(f'#{tc} {n[2]}')
    elif n[0] == n[2]:
        print(f'#{tc} {n[1]}')
    else:
        print(f'#{tc} {n[0]}')