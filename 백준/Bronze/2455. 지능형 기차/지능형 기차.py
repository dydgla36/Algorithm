cnt,r = 0,0
for i in range(4):
    m,p = map(int,input().split())
    cnt += p-m
    if cnt > r:
        r = cnt
print(r)