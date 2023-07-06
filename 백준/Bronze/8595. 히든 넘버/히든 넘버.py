import sys
input = sys.stdin.readline
import re

num = int(input())
nums = str(input())

sum = 0

for i in re.split('[^0-9]', nums):
    if i != "":
        sum += int(i)

print(sum)