import sys

t, x, m = map(int, sys.stdin.readline().strip().split())

if m == 0:
    print(t * x)
    exit()

min_x = float('inf')
for _ in range(m):
    d, s = map(int, sys.stdin.readline().strip().split())
    min_x = min(min_x, (d-1)//s)

if min_x == 0:
    print(0)
elif t > min_x:
    print((min_x + ((t - min_x)//2)) * x)
else:
    print(t * x)
