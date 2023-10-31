T = int(input())
a = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
    case = str(input())
    yy = case[0:4]
    mm = case[4:6]
    dd = case[6:8]
    answer = "-1"
    if 0 < int(mm) < 13 and 0 < int(dd) <= a[int(mm)]:
        answer = yy + '/' + mm + '/' + dd
    print("#{} {}".format(test_case, answer))