n, l = map(int, input().split())
for i in range(l, 101):
    x = n - (i * ( i + 1 ) // 2)
    if x % i == 0:
        xx = x // i
        if xx + 1 >= 0:
            print(*(i for i in range(xx + 1, xx + i + 1)))
            break
else:
    print(-1)