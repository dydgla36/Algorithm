n = int(input())

for i in range(n):
    score = 0
    plus = 1 
    scoreL = input()
    for j in range(len(scoreL)):

        if scoreL[j] == 'O':
            score +=plus
            plus+=1


        elif scoreL[j] == 'X':
            plus =1
    print(score)