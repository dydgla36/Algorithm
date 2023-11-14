for tc in range(1, int(input()) + 1):
    n = int(input())
    money = list(map(int, input().split()))
    money.sort()
    value = sum(money) // len(money)
    cnt = 0
    for i in range(len(money)):
        if value >= money[i]:
            cnt += 1
        else:
            break
    print(f'#{tc} {cnt}')
