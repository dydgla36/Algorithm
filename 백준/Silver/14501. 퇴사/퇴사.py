import sys
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    data.append(list(map(int, input().split())))

day = [0] * (n+1)

for i in range(1,n+1):
    t, p = data[i-1][0], data[i-1][1]
    if i+t-1 <= n:
        day[i+t-1] = max(day[i+t-1], day[i-1] + p)
    if day[i] < day[i-1] :
        day[i] = day[i-1]
        
print(max(day))