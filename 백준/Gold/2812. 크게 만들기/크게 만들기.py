# numbers에 있는 숫자를 하나씩 stack에 넣고 그 다음 숫자와 비교
# 만일 다음 숫자가 stack에 있는 숫자보다 크면 stack.pop()을 해주면서 가장 큰 숫자를 앞 쪽에 위치하도록 한다.
# k개 까지만 지워야 하므로 k > 0이상일 때만 수행하고, 만일 k개 미만으로 숫자를 지웠다면 뒤에 있는 숫자를 남은 k개 만큼 지우고 출력한다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = input().rstrip()
stack = []
for number in numbers:
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))