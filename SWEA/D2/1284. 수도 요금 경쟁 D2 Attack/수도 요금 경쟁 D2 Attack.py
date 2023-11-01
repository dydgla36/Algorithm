T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W - R > 0:
        B = (W - R) * S + Q
    else: 
        B = Q
        
    if A > B:
        print("#{} {}".format(test_case, B))
    else:
        print("#{} {}".format(test_case, A))