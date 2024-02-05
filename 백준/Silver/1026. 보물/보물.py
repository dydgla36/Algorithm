num = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
temp = b
a = sorted(a)
sum = 0
for i in range(num): 
    sum += (a[i] * temp[temp.index(max(temp))])
    temp.remove(max(temp))
print(sum)