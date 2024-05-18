li = []
for _ in range(8):
    li.append(int(input()))
res = sorted(li)[3:]
tmp = []
print(sum(res))
for i in res:
    tmp.append(li.index(i)+1)
print(*sorted(tmp))