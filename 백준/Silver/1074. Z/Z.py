import sys                    #많이 어려움
input = sys.stdin.readline

result = 0

def z(n, x, y):
    global result           # result를 전역변수로 저장
    if x == r and y == c:   # 위치를 찾았을 때
        print(int(result))  # 위치값을 출력
        return

    if n == 1:              
        result += 1
        return
    # x
    if not (x <= r < x + n and y <= c < y + n):     #몇 사분면인지 찾는 작업
        result += n * n
        return
    z(int(n / 2), x, y)                             #1사분면            
    z(int(n / 2), x, y + int(n / 2))                #2사분면
    z(int(n / 2), x + int(n / 2), y)                #3사분면
    z(int(n / 2), x + int(n / 2), y + int(n / 2))   #4사분면

n, r, c = map(int, input().split())
z(2 ** n, 0, 0)                     #입력 받은 n의 값의 2의 n제곱을 넣어줌 그래야 큰 틀을 잡아서 분할탐색가능


# import sys                    
# input = sys.stdin.readline

# N, r, c = map(int, input().split())

# ans = 0

# while N != 0:

# 	N -= 1

# 	# 1사분면
# 	if r < 2 ** N and c < 2 ** N:
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 0

# 	# 2사분면
# 	elif r < 2 ** N and c >= 2 ** N: 
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 1
# 		c -= ( 2 ** N )
        
# 	# 3사분면    
# 	elif r >= 2 ** N and c < 2 ** N: 
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 2
# 		r -= ( 2 ** N )
        
# 	# 4사분면    
# 	else:
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 3
# 		r -= ( 2 ** N )
# 		c -= ( 2 ** N )
    
# print(ans)
