grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    data = []
    for i in range(n):
        a, b, c = map(int, input().split())
        sum_value = (a * 0.35) + (b * 0.45) + (c * 0.2)
        data.append(sum_value)
    score = data[k-1]
    data.sort(reverse=True)

    value = n // 10
    result = data.index(score) // value
    print(f'#{tc} {grade[result]}')