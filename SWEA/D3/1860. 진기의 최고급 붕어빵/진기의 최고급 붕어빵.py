t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    result = "Possible"
    for i in range(n):
        bread = (arrive[i] // m) * k - (i + 1)
        if bread < 0:
            result = "Impossible"
            break
    print(f'#{tc} {result}')