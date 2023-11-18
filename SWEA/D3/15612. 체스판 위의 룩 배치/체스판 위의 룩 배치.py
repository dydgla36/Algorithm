for tc in range(1, int(input()) + 1):
    chessboard = [list(input()) for _ in range(8)]
    rotated_chessboard = list(zip(*chessboard[::-1]))   # 체스판을 90도 회전 시켜서 2차원 배열로 받음
    result = True

    for i in range(8):
        # 가로줄에도 'O'가 하나여야 하고
        if chessboard[i].count('O') != 1:
            result = False
            break
        # 세로줄에도 'O'가 하나여야 한다
        if rotated_chessboard[i].count('O') != 1:
            result = False
            break
    if result:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')