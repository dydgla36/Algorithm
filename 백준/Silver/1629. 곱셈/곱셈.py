import sys
input = sys.stdin.readline
      
A, B, C = map(int, input().split())

# 분할정복
def power(a, b):
    if b == 1:  # b의 값이 1이 될 때까지 재귀
        return a % C
    else:
        tmp = power(a, b // 2)  # a^(b // 2)
        if b % 2 == 0:
            return tmp * tmp % C  # b가 짝수인 경우
        else:
            return tmp * tmp * a % C  # b가 홀수인 경우

res = power(A, B)
print(res)
      
#def abc(a, b, c):
#    if b == 1:                              # 아래식처럼 하면 1//2 는 0이므로 1은 나머지 구하는것을 먼저 확인한다
#        return a % c
#    elif b % 2 == 0:                        
#        return (abc(a,b//2,c)**2)%c
#    else:
#        return ((abc(a,b//2,c)**2)*a)%c

# num = list(map(int, input().split()))
# print(abc(num[0], num[1], num[2]))

