t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    num = list(map(int, input().split()))
    value = num[0]
    for i in range(n - 1):
        if num[i] >= 0 and (num[i] + num[i+1] >= 0):
            num[i+1] += num[i]
        if value < num[i+1]:
            value = num[i+1]
    print(f'#{tc} {value}')
