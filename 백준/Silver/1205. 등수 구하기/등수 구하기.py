n, s, p = map(int, input().split())
if n == 0:
    print(1)
else:
    st = list(map(int, input().split()))
    if n == p and st[-1] >= s:
        print(-1)
    else:
        temp = n + 1
        for i in range(n):
            if st[i] <= s:
                temp = i + 1
                break
        print(temp)