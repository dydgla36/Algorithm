import sys
input = sys.stdin.readline
N = int(input())        #26을 입력 받으면
cnt = 0                 #0을 초기화

first = N // 10       # 26 // 10 = 2 값을 first에 넣음
second = N % 10       # 26 % 10 = 6 값을 second에 넣음
add = (second * 10) + ((first + second) % 10)     # (6 * 10) + ((2+6) % 10) = 68
cnt += 1 

while N > 0:     
  first = add // 10       # 68 // 10 = 6 값을 first에 넣음
  second = add % 10       # 68 % 10 = 8 값을 second에 넣음
  add = (second * 10) + ((first + second) % 10)     # (8 * 10) + ((6 + 8) % 10) = 84
  cnt += 1                                          # 카운트라는 변수를 통해 몇번만에 돌아오는지 확인하기위해 1씩 증가 
  
  if (add == N):                                    # 84이라는 값이 26가 같으면 break 지금은 아니므로 다시 while문 처음으로 다시 돌아감
    break 

print(cnt)
