num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
t = int(input())
for tc in range(1, t + 1):
    test, num = map(str, input().split())
    num_chr = list(map(str, input().split()))
    result = []
    for i in range(10):
        cnt = 0
        for j in num_chr:
            if j == num_list[i]:
                cnt += 1
        result += [num_list[i]] * cnt
    print(test)
    print(*result)
    


