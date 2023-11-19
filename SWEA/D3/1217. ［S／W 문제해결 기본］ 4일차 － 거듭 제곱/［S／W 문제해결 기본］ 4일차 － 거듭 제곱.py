def power(n, m):
    if m == 0:
        return 1
    else:
        return n * power(n, m-1)

for tc in range(1, 11):
    test_case = int(input())
    n, m = map(int, input().split())
    result = power(n, m)
    print(f'#{test_case} {result}')
