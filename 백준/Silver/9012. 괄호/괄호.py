import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = []
    round = input()
    for j in round:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack: #stack이 채워져있어야
                stack.pop()
            else:
                print("NO") 
                break
    else:
        if not stack:
            print("YES")
        else: 
            print("NO")
