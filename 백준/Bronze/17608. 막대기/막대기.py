import sys
input = sys.stdin.readline

N = int(input())
h = []
count = 1
for i in range(N):
    h.append(int(input()))
standard = h[-1]
while h:
    if standard < h[-1]:
        standard = h.pop()
        count += 1
    else :
        h.pop()
print(count)
        
    