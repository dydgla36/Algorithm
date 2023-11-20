N = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N
for i in Ai:
    i -= B
    if i > 0:
        if i % C:
            cnt += (i // C) + 1
        else:
            cnt += (i // C)
print(cnt)

