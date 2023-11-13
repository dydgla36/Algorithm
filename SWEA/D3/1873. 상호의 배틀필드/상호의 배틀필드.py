move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
command = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3, 'S' : 4,
'^' : 0, 'v' : 1, '<': 2, '>' : 3, 0 : '^', 1 : 'v', 2 :'<', 3 :'>'}
search = ['<', '>', '^', 'v']
t = int(input())
for tc in range(1, t + 1):
    h, w = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    n = int(input())
    st = list(input())

    for i in range(h):
        for j in range(w):
            if maps[i][j] in search:
                tank = (i,j,command[maps[i][j]])
               
    for com in st:
        control = command[com]
        if control == 4:
            dy = tank[0]
            dx = tank[1]
            while True:
                dy += move[tank[2]][0]
                dx += move[tank[2]][1]
                if 0 > dy or dy >= h or 0 > dx or dx >= w or maps[dy][dx] == '#':
                    break
                if maps[dy][dx] == '*':
                    maps[dy][dx] = '.'
                    break
        else:
            y = tank[0]
            x = tank[1]
            dy = y + move[control][0]
            dx = x + move[control][1]
            maps[y][x] = command[control]
            tank = (y,x,control)
            if 0 <= dy and dy < h and 0 <= dx and dx < w and maps[dy][dx] == '.':
                maps[y][x] = '.'
                maps[dy][dx] = command[control]
                tank = (dy, dx, control)
    print(f'#{tc}', end = " ")
    for m in maps:
        print(''.join(m))
