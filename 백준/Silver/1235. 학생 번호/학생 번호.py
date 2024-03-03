n = int(input())
numbers = []
for _ in range(n):
    numbers.append(str(input()))
for i in range(1, len(numbers[0])+1):
    results = []
    for j in range(n):
        if numbers[j][-i:] in results:
            break
        else:
            results.append(numbers[j][-i:])
    if len(results) == n:
        print(i)
        break