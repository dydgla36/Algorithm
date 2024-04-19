n = int(input())
f = [1, 1]
for i in range(2, 21):
    f.append(f[i-1]*i)
sum = 0
for i in range(20, -1, -1):
    if sum+f[i] < n:
        sum += f[i]
    elif sum+f[i] == n:
        print("YES")
        exit(0)
print("NO")