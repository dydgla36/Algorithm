import sys
input = sys.stdin.readline
      
def abc(a, b, c):
    if b == 1:                              # 아래식처럼 하면 1//2 는 0이므로 1은 나머지 구하는것을 먼저 확인한다
        return a % c
    elif b % 2 == 0:                        
        return (abc(a,b//2,c)**2)%c
    else:
        return ((abc(a,b//2,c)**2)*a)%c

num = list(map(int, input().split()))
print(abc(num[0], num[1], num[2]))