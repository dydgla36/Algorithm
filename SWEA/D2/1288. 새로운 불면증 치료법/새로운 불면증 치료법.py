T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    cnt = 0
    data = [0] * 10
    while True:
        if 0 not in data:
       		break
       	else:
            cnt += 1
            temp = str(n * cnt)
            for j in range(len(temp)):
                data[int(temp[j])] = 1
    print("#{} {}".format(test_case, temp))