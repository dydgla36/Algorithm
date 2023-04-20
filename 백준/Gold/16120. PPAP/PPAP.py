import sys
input = sys.stdin.readline
list = input().strip()
stack = []
for i in list:
    stack.append(i)
    if stack[-4:] == ["P", "P", "A", "P"]:
        stack.pop()
        stack.pop()
        stack.pop()
if stack == ["P"]:
    print("PPAP")
else:
    print("NP")