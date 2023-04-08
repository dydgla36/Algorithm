N = int(input())
a = list(map(int, input().split()))   
result =0
for i in range(N):    # i를 a까지 증가
    
    cnt = 0     # cnt를 0으로 초기화
    for j in range(2, a[i]+1) :   
        if a[i]%j == 0 :
            cnt += 1
    if cnt == 1 :
        result += 1
print(result)