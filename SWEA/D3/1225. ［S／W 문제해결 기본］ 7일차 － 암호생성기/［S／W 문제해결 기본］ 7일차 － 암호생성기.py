for tc in range(1, 11):
    t = int(input())
    num = list(map(int, input().split()))
    while num[-1] != 0:
        for i in range(1, 6):
            num.append(num.pop(0) - i)
            if num[-1] <= 0:
                num[-1] = 0
                break
    print(f'#{t}',end = " ")
    print(*num)