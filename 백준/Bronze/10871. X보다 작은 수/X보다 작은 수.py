n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in a:
    if i < x :
        print("%d" % i,end = ' ')