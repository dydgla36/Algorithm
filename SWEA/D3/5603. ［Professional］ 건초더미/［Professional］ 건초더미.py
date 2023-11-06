t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))
    value = sum(data) / n
    result = 0
    for j in range(len(data)):
        if data[j] >= value:
            result += data[j] - value
    print(f'#{tc} {int(result)}')