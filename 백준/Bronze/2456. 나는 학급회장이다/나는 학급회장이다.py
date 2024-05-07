N = int(input())
case = [
        {'name':1,1:0,2:0,3:0,'total' :0}, 
        {'name':2, 1:0,2:0,3:0,'total' :0}, 
        {'name':3, 1:0,2:0,3:0,'total' :0}
        ]
for _ in range(N) :
    a,b,c = map(int,input().split())
    case[0][a] += 1
    case[1][b] += 1
    case[2][c] += 1
    case[0]['total'] += a
    case[1]['total'] += b
    case[2]['total'] += c
case.sort(key = lambda x : (x['total'],x[3],x[2],x[1]),reverse = True)
if case[0]['total'] ==case[1]['total'] and case[0][3]==case[1][3] and case[0][2]==case[1][2] : print(0,case[0]['total'])
else : print(case[0]['name'],case[0]['total'])