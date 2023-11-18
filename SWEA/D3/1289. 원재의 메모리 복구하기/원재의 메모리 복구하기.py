for tc in range(1, int(input()) + 1):
    n = input()
    flag = "0"
    cnt = 0
    for i in range(len(n)):
        if n[i] != flag:
            flag = n[i]
            cnt += 1
    print(f'#{tc} {cnt}')