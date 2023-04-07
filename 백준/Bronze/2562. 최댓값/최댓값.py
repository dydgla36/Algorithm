lst = []
for i in range(9):
  n = int(input())
  lst.append(n)

max = 0
for i in lst:
  if max<i:
    max = i
    cnt = lst.index(i)+1
print(max)
print(cnt)
