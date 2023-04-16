# 참조 : https://western-sky.tistory.com/140
import sys
input = sys.stdin.readline

m, n, l = map(int, input().split()) # m = 사대의수, n = 동물의수, l = 사정거리
gun = list(map(int, input().split()))  #사대의 좌표
animal = list(map(int, input().split()) for _ in range(n)) #동물의 좌표
gun.sort()  #사대의 좌표 정렬
cnt = 0 #동물 잡은수

for x, y in animal: #동물을 좌표를 고정하고 사대를 기준으로 잡을 수 있는 사대 있는지 확인
    if (y>l):       #y좌표가 사정거리보다 크면 당연히 쏠 수 없음 그래서 그 다음 for문 돌려줌
        continue
    min = x+y-l     #동물을 잡을 수 있는 최소 좌표  
    max = x-y+l     #동물을 잡을 수 있는 최대 좌표  
    left, right = 0, m-1
    while left <= right:
        mid = (left+right)//2       
        if gun[mid] >= min and gun[mid] <= max: 
            cnt += 1
            break
        elif gun[mid] < max:    
            left = mid + 1
        else:
            right = mid - 1
print(cnt)