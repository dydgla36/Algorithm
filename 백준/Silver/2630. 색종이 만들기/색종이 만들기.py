import sys
input = sys.stdin.readline

def folding(x, y, n):
    c_paper = paper[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if c_paper != paper[i][j] :
                folding(x, y, n//2)             # 1사분면
                folding(x+n//2, y, n//2)        # 2사분면
                folding(x, y+n//2, n//2)        # 3사분면  
                folding(x+n//2, y+n//2, n//2)   # 4사분면
                return
    if c_paper == 0 :
        result.append(0)
    else :
        result.append(1)
    
    
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

result = []

folding(0,0,n)
print(result.count(0))
print(result.count(1))