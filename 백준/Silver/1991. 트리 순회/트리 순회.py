import sys
input = sys.stdin.readline
n=int(input())
tmp={}
for _ in range(n):
    a,b,c=input().split()
    tmp[a]=[b,c]
def pre(x):
    if x!=".":
        print(x,end="")
        pre(tmp[x][0])
        pre(tmp[x][1])
def In(x):
    if x!=".":
        In(tmp[x][0])
        print(x,end="")
        In(tmp[x][1])
def post(x):
    if x!=".":
        post(tmp[x][0])
        post(tmp[x][1])
        print(x,end="")
pre('A')
print()
In('A')
print()
post('A')