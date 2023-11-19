for tc in range(1, int(input()) + 1):
    n = int(input())

    # (0,0)점 한개 + 각 꼭짓점 4개 + x축 y축에 걸쳐있는 (n-1)개의 점 * 4(4분면)
    points = (n - 1) * 4 + 5
    cnt = 0

    for i in range(1, n):
        for j in range(1, n):
            if (i ** 2) + (j ** 2) <= n ** 2:
                cnt += 1

    points += (cnt * 4)
    print(f'#{tc} {points}')