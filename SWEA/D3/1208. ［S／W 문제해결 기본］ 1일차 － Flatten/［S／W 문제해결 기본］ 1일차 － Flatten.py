for tc in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))
    for i in range(n):
        max_data = data.index(max(data))
        min_data = data.index(min(data))
        data[max_data] -= 1
        data[min_data] += 1
    result = max(data) - min(data)
    print(f'#{tc} {result}')