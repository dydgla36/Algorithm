a = int(input())
b = int(input())
c = int(input())
d = list(str(a*b*c))
e = [0] * 10
for i in range(0,10):
    for j in d:
        if str(i) == j:
            e[i] += 1
for k in e:
    print(k)
        
