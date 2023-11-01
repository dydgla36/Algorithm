T = int(input())
for test_case in range(1, T + 1):
    st = input()
    for i in range(1,10):
        if st[ : i] == st[ i : 2 * i]:
            print("#{} {}".format(test_case, i))
            break