for tc in range(1, 11):
    t = int(input())
    n, m = map(int,input().split())
    value = n ** m
    print(f'#{t} {value}')