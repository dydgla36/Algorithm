def dfs(c, v):
    global cnt
    cnt = max(cnt, len(v))
    for n in data[c]:
        if n not in v:
            dfs(n, v+[n])

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    data = [[] for _ in range(n+1)]
    for i in range(m):
        x, y = map(int, input().split())
        data[x].append(y)
        data[y].append(x)


    cnt = 0
    for x in range(1, n + 1):
        dfs(x, [x])


    print(f'#{tc} {cnt}')