import sys
input = sys.stdin.readline
N, M = map(int, input().split())  
square = []
for _ in range(N):
    square.append(list(input()))
size = min(N, M)
for k in range(size, 0, -1):
    for i in range(N):
        for j in range(M):
            if ((i + k) < N) and ((j + k) < M) and (square[i][j] == square[i][j + k] == square[i + k][j] == square[i + k][j + k]):
                print((k+1)**2)
                exit()
else:
    print(1)