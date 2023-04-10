from itertools import combinations  #라이브러리 사용하여 

heights=[int(input()) for _ in range(9)] 
for combi in combinations(heights,7):   
    # combinations라는 함수는 인풋으로 리스트와 정수를 받는다
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    # 받은 값들에서 7개를 뽑아서 경우의수 중 7개의 총합이 100이 되면 
    if sum(combi)==100: 
        for height in sorted(combi):    # 7개의 총합이 100이 된 값들을 오름차순으로 정렬
            print(height)   
        break
    
# list=[] # 리스트를 배열로 받음 
# for i in range(9):
#     list.append(int(input()))   #리스트에 입력받은 값을 추가함
# c=0     # for문 끝내기
# over=sum(list)-100  # over에 리스트에 받은 값을 다 더해서 -100를 한 값을 저장
# #9명의 난쟁이 수의 합이 140인데 100빼서 40이라는 값을 9명중에 2명을 더 했을때 값이 40성공
# for j in range(9):
#     for k in range(9):
#         if j==k: continue       #같은 난쟁이가 2번 들어가면 안됨
#         if list[j]+list[k]==over:   #두 난쟁이 합이 40이면  
#             if j<k:                 
#                 list.pop(j)     #j위치에 있는 난쟁이 끄집어냄
#                 list.pop(k-1)   #k-1위치에 있는 난쟁이 끄집어냄 (왜 -1이 필요한지 잘 모름) 
#             else: 
#                 list.pop(k)     #k위치에 있는 난쟁이 끄집어냄
#                 list.pop(j-1)   #j-1위치에 있는 난쟁이 끄집어냄 (왜 -1이 필요한지 잘 모름)
#             c=1
#             break
#     if c==1:
#         break

# list.sort() # 7개의 총합이 100이 된 값들을 오름차순으로 정렬
# for _ in list:
#     print(_)