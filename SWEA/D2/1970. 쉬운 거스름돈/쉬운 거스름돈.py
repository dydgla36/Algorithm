t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, t + 1):
    n = int(input())
    coin = [0] * 8
    for i in range(8):
        if n // money[i] > 0:
            coin[i] += n // money[i]
            n = n % money[i]
    print(f'#{tc} ')
    print(*coin)
