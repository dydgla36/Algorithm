for tc in range(1, 11):
    n = int(input())
    data = [list(map(str, input())) for _ in range(100)]
    max_length = 0
    for length in range(100, 0, -1):  
        for i in range(100):
            for j in range(100 - length + 1):
                if data[i][j:j+length] == data[i][j:j+length][::-1]:
                    max_length = length
        for j in range(100):
            for i in range(100 - length + 1):
                col = [data[k][j] for k in range(i, i+length)]
                if col == col[::-1]:
                    max_length = length
        if max_length:
            break
    print(f'#{tc} {max_length}')