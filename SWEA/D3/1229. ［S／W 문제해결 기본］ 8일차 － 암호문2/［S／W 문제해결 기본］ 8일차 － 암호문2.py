for tc in range(1, 11):
    n = int(input())
    or_pw = list(map(int, input().split()))
    com_num = int(input())
    com = list(map(str, input().split()))

    for i in range(len(com)):
        if com[i] == 'I':
            x = int(com[i+1])
            y = int(com[i+2])
            for j in range(y):
                or_pw.insert(x+j, com[i+3+j])
        if com[i] == 'D':
            x = int(com[i+1])
            y = int(com[i + 2])
            del or_pw[x:x + y]

    print(f'#{tc}', end=" ")
    print(*or_pw[:10])