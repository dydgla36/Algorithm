from datetime import date
strptime = lambda: date(**{k:int(v) for k,v in zip(['year','month','day'],input().split())})
today, dday = strptime(), strptime()
if dday >= today.replace(today.year+1000):
    print('gg')
else:
    print('D-'+str((dday-today).days))