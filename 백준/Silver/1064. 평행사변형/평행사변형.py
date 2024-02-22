xa,ya,xb,yb,xc,yc = map(int,input().split())
if ((xa-xb)*(ya-yc) == (xa-xc)*(ya-yb)):
    print(-1.0)
    quit()
ab = ((xa-xb)**2+(ya-yb)**2)**0.5
bc = ((xa-xc)**2+(ya-yc)**2)**0.5
ca = ((xb-xc)**2+(yb-yc)**2)**0.5
tmp = [ab+bc,ab+ca,bc+ca]
result = max(tmp)-min(tmp)
print(result*2)