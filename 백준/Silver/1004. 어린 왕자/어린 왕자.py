T = int(input())

for i in range(T):
    count = 0
    x1,y1,x2,y2=map(int,input().split())
    num=int(input())
    for i in range(num):
        cx,cy,r = map(int,input().split())
        a=((x1-cx)**2+(y1-cy)**2)**0.5
        b=((x2-cx)**2+(y2-cy)**2)**0.5
        if a < r or b < r:
            if a < r and b < r:
                pass
            else:
                count += 1
    print(count)