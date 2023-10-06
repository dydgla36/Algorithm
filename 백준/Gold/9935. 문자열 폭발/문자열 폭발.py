st = input()
de = list(input())
stack = []
for i in range(len(st)):
    stack.append(st[i]) # 스택에 하나씩 추가
    if stack[-len(de):] == de: # 스택의 마지막이 m 문자열과 같으면
        del stack[-len(de):] # 삭제
if stack: print("".join(stack))
else: print("FRULA")