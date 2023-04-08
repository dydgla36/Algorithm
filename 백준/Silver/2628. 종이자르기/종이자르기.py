x, y = map(int, input().split())
yyy = [0,y]
xxx = [0,x]
t = int(input())
for i in range(t):
    xx, yy = list(map(int, input().split()))
    if xx == 0:
        yyy.append(yy)
    else :
        xxx.append(yy)
yyy.sort()
xxx.sort()
max_x = 0; max_y = 0
for j in range(len(yyy)-1,0,-1):
    yyyy = yyy[j] - yyy[j-1]
    if max_y < yyyy:
        max_y = yyyy
for k in range(len(xxx)-1,0,-1):
    xxxx = xxx[k] - xxx[k-1]
    if max_x < xxxx:
        max_x = xxxx
print(max_x * max_y)