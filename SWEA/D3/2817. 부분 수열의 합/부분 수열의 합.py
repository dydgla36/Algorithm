def dfs(x, y):
    global cnt
    if k < y:
        return 
    if x == n:
        if y == k:
            cnt += 1
        return 
    dfs(x+1, y+data[x])
    dfs(x+1, y)


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0

    dfs(0, 0)
    print(f'#{tc} {cnt}')
