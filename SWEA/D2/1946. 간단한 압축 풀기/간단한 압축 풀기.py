T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case} ')
    temp = ''
    for _ in range(n):
        a, b = input().split()
        b = int(b)
        for _ in range(b):
            temp += a
            while len(temp) >= 10:
                print(temp[:10])
                temp = temp[10:]
    print(temp)
