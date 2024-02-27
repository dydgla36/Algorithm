n, k = map(int, input().split())
list = [i for i in range(1, n + 1)]
answer = []
num = 0
for i in range(n):
    num += k - 1
    if num >= len(list):
        num %= len(list)
    answer.append(str(list.pop(num)))
print("<", ", ".join(answer), ">", sep='')