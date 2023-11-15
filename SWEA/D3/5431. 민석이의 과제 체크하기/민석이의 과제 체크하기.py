for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    student = list(map(int, input().split()))
    student.sort()
    result = []
    for i in range(1, n + 1):
        if i not in student:
            result.append(i)
    print(f'#{tc} ',end="")
    print(*result)