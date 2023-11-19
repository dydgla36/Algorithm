for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    data = [[0] * (n + 1) for _ in range(n + 1)]
    mm = n // 2
    data[mm][mm] = data[mm+1][mm+1] = 2
    data[mm][mm+1] = data[mm+1][mm] = 1

    for i in range(m):
        x, y, c = map(int, input().split())
        data[x][y] = c
        for di, dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
            r = []
            for mul in range(1, n):
                ni, nj = x + di * mul, y + dj * mul
                if 1 <= ni <= n and 1 <= nj <= n:
                    if data[ni][nj] == 0:
                        break
                    elif data[ni][nj] == c:
                        while r:
                            ti, tj = r.pop()
                            data[ti][tj] = c
                        break
                    else:
                        r.append((ni, nj))
                else:
                    break

    bcnt = wcnt = 0
    for lst in data:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')