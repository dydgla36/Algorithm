n=int(input())
k=int(input())
s = [0 for i in range(n+1)]
for i in range(2,n+1):
    if s[i] == 0:
        for j in range(i,n+1,i):
            if j%i == 0:
                s[j] = max(s[j],i)
ans=0
for i in s:
    if i<=k:
        ans+=1
print(ans-1)