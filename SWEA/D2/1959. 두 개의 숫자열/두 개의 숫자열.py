t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_value = 0
    if n < m:
        for i in range(m - n + 1):
            value = 0
            for j in range(n):
                value += a[j]*b[i+j]
            if value > max_value :
                max_value = value
    else:
        for i in range(n - m + 1):
            value = 0
            for j in range(m):
                value += a[i+j]*b[j]
            if value > max_value:
                max_value = value
    print(f'#{tc} {max_value}')

