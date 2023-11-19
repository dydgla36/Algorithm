for tc in range(1, 11):
    n = int(input())
    data = [list(map(str, input())) for _ in range(100)]
    r_data = list(map(list, zip(*data)))  # data의 행과 열을 바꿈
    max_length = 0
    for length in range(100, 0, -1):
        for i in range(100):
            for j in range(100 - length + 1):
                if data[i][j:j+length] == data[i][j:j+length][::-1]:
                    max_length = length
        for i in range(100):
            for j in range(100 - length + 1):
                if r_data[i][j:j+length] == r_data[i][j:j+length][::-1]:  # r_data를 사용하여 각 열에서 회문 찾기
                    max_length = length
        if max_length:
            break
    print(f'#{tc} {max_length}')
