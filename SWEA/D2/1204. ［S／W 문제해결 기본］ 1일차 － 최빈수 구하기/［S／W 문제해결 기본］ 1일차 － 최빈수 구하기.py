T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))
    storage = [0] * 1001
    
    for i in score:
        storage[i] += 1
        
    max_score = max(storage)
    result = []
    
    for j in range(len(storage)):
        if storage[j] == max_score:
            result.append(j)
    print("#{} {}".format(test_case, max(result)))