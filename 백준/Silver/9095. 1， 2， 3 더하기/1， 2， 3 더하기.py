import sys
input = sys.stdin.readline
T = int(input())
result = []

def dfs(num,sum):
    global count
    # 더한 값이 구하는 값보다 크다면 리턴
    if num < sum:
        return
    # 더한 값이 구한 값과 같다면 개수 추가
    if num == sum:
        count += 1
        return
    #
    for i in range(1,4):
        sum += i
        dfs(num,sum)
        sum -= i    #재귀할 때 값을 원래대로 돌려줌
    
for _ in range(T):
    
    num = int(input())
    count = 0
    dfs(num,0)
    result.append(count)
    
for answer in result:
    print(answer)
                





