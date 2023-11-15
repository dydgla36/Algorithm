day = {"MON" : 6, "TUE" : 5, "WED" : 4, "THU" : 3 , "FRI" : 2, "SAT" : 1, "SUN" : 7}
for tc in range(1, int(input()) + 1):
    today = input()
    if today in day:
        print(f'#{tc} {day[today]}')