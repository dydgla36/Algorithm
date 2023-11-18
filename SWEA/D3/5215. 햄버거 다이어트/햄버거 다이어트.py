for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    s = []
    k = []

    def dfs(i, taste, kcal):
        global max_taste
        if kcal > L:  # 칼로리 초과
            return
        if taste > max_taste:  # 최대 칼로리 저장
            max_taste = taste
        if i == N:  # 끝
            return
        dfs(i + 1, taste + s[i], kcal + k[i])  # 현재 재료 선택
        dfs(i + 1, taste, kcal)  # 현재 재료 미선택


    for _ in range(N):
        score, kcal = map(int, input().split())
        s.append(score)
        k.append(kcal)
    max_taste = 0
    dfs(0, 0, 0)
    print(f'#{tc} {max_taste}')