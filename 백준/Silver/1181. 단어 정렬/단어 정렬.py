import sys
input = sys.stdin.readline

n = int(input())
words = list({input().rstrip() for _ in range(n)})  #문자열 오른쪽 뒤 제거
words.sort(key = lambda x : (len(x), x))

for word in words:
    print(word)