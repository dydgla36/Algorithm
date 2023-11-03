t = int(input())
for tc in range(1, t + 1):
    n = list(map(int,input().split()))
    n.sort()
    value = sum(n[1:9])
    result = round(value / 8)
    print(f'#{tc} {result}')