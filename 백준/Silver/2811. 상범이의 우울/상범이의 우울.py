import sys
input = sys.stdin.readline
N = int(input())
table = list(map(int, input().split()))
flower = [0] * N
length = 0
maxlength = 0
for i in range(N - 1, -1, -1):
    if table[i] < 0:
        length += 1
        continue
    for j in range(0, length * 2):
        if (i - j) > -1:
            flower[i - j] = 1
    maxlength = max(maxlength, length)
    length = 0
ans = 0
for f in flower:
    if f == 1:
        ans += 1
maxidx = 0
maxcount = 0
length = 0
for i in range(N - 1, -1, -1):
    if table[i] < 0:
        length += 1
        continue
    if length == maxlength:
        count = 0
        for j in range(0, length * 3):
            if (i - j) > -1 and flower[i - j] == 0:
                count += 1
        if count > maxcount:
            maxcount = count
            maxidx = i
    length = 0
print(ans + maxcount)