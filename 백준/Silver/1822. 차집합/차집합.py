N = map(int, input().split())
A =set(map(int, input().split()))
B = set(map(int, input().split()))
temp = A-B
res = sorted(temp)
print(len(res))
if len(res) !=0:
    print(*(res))