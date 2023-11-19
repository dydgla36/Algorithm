for tc in range(1, 11):
    n = int(input())
    data = [list(map(str, input())) for _ in range(8)]
    r_data = list(map(list, zip(*data)))  # data의 행과 열을 바꿈
    cnt = 0
    for i in range(8):
        for j in range(8 - n + 1):
            if data[i][j:j+n] == data[i][j:j+n][::-1]:
                cnt += 1
    for i in range(8):
        for j in range(8 - n + 1):
            if r_data[i][j:j+n] == r_data[i][j:j+n][::-1]:  # r_data를 사용하여 각 열에서 회문 찾기
                cnt += 1
    print(f'#{tc} {cnt}')
