t = int(input())
for tc in range(1, t + 1):
    data = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        r = [0] * 10
        c = [0] * 10
        for j in range(9):
            r[data[i][j]] += 1
            c[data[j][i]] += 1
        for k in range(1, 10):
            if r[k] != 1 or c[k] != 1:
                result = 0
                break
    for i in range(3):
        for j in range(3):
            n = [0] * 10
            for k in range(3):
                for l in range(3):
                    n[data[3*i+k][3*j+l]] += 1
            for m in range(1,10):
                if n[m] != 1:
                    result = 0
                    break
    print(f'#{tc} {result}')

