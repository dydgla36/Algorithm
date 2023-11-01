T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result =[]
    for i in range(n):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:	#첫번째거나 마지막이면 
                temp.append(1)
            else:						#
                temp.append(result[i-1][j] + result [i-1][j-1])
        result.append(temp)
    print('#%d' % test_case)
    for k in result:
        print(*k)