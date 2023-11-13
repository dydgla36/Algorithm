t = int(input())
for tc in range(1, t + 1):
    p, q = map(int, input().split())
    x1 = x2 = y1 = y2 = pp = qq = 0
    for i in range(10000):
        if p > 0:
            p = p - i
            pp = i
        if q > 0:
            q = q - i
            qq = i
        

    x1 = pp + p
    y1 = abs(p) + 1
    x2 = qq + q
    y2 = abs(q) + 1

    result_x = x1 + x2
    result_y = y1 + y2
    result = 0
    len_res = result_x + result_y
    for i in range(len_res - 1):
        result += i
    result += result_x
    print(f'#{tc} {result}')