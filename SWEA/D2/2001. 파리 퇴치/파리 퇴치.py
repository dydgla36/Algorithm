t = int(input())
dc = [1, 0, -1, 0]
dr = [0, 1, 0, -1]
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n-m+1):
        for j in range(n - m + 1):
            value = 0
            for x in range(i, i + m):
                for y in range(j, j + m):
                    value += data[x][y]
            if result < value:
                result = value
    print(f'#{tc} {result}')