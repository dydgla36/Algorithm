T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    print("#{} {} {}".format(test_case, n//m, n%m))