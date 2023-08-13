import sys
input = sys.stdin.readline

stack_left = list(input().strip())
stack_right = []
m = int(input())
n = len(stack_left)

for i in range(m):
    command = input().strip()

    if command[0] == "P":
      stack_left.append(command[2])
    elif command[0] == "L" and stack_left != []:
      stack_right.append(stack_left.pop())
    elif command[0] == "D" and stack_right != []:
      stack_left.append(stack_right.pop())
    elif command[0] == "B" and stack_left != []:
      stack_left.pop()  

print("".join(stack_left + list(reversed(stack_right))))
