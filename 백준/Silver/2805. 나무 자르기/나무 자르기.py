import sys
input = sys.stdin.readline

def search(goal): # 이진 탐색
    low_idx = 0
    high_idx = 1000000000
    while low_idx <= high_idx:  
        mid_idx = (low_idx + high_idx) //2 
        if cut(mid_idx) >= goal:
            low_idx = mid_idx + 1
        elif cut(mid_idx) < goal:
            high_idx = mid_idx - 1
            
    print(high_idx)
    
def cut(cut_height):    #자르기
    sum = 0
    for i in t_height:
        remain = i - cut_height
        if remain > 0:
            sum += remain
    return sum    

number, need = map(int,input().split())
t_height = list(map(int, input().split()))
search(need)