for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    value = 0
    for i in range(k):
        value += score[i]
    print(f'#{tc} {value}')
