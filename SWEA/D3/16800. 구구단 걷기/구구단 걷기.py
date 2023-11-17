for tc in range(1, int(input()) + 1):
    n = int(input())
    n1 = 10**12
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            n1 = min(n1, i + j)

    print(f'#{tc} {n1 - 2}')