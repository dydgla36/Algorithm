for tc in range(1, int(input()) + 1):
    n, d = map(int, input().split())
    cnt = d * 2 + 1
    result = n // cnt
    if n % cnt != 0:
        result += 1
    print(f'#{tc} {result}')