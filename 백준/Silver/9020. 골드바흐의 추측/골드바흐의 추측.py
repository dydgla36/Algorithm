t = int(input())

a = [int(input()) for _ in range(t)]    
b = max(a)
num = 2
count = 0
lst = []
e = [0] * (b+1)
while num <= b:
    i = 2  # 2 ~ num 까지 증가할 변수
    while num % i:  # 나머지 있으면(예) 1,2,3) 안으로 들어감
        i += 1      # 1증가

    if i == num:  # 나누어진 수가 자기 자신이면 소수
        lst.append(num)
        e[num] = 1
    num += 1

for j in a:
    s = j//2
    for k in range(s,1,-1):
        if e[k] == 1 and e[j-k] == 1:
            print(k,j-k)
            break
