import sys
input = sys.stdin.readline

sum = 0
stack = []
k = int(input())
for i in range(k):
    arr = int(input())
    if arr == 0:
        stack.pop()
    else:
        stack.append(arr)
for i in range(len(stack)):
    sum += stack[i]
print(sum)
    
