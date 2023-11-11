for tc in range(1, 11):
    n, numbers = input().split()
    n = int(n)
    numbers = list(numbers)
    flag = True
    while flag:
        for i in range(1, len(numbers) + 1):
            if numbers[i] == numbers[i - 1]:
                del numbers[i]
                del numbers[i - 1]
                break
            if i == len(numbers) - 1:
                flag = False
                break
    print(f'#{tc}', end=" ")
    print(*numbers, sep='')
