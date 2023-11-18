a = 'abcdefghijklmnopqrstuvwxyz'
for tc in range(1, int(input()) + 1):
    s = input()
    cnt = 0
    for i in range(len(s)):
        if a[i] == s[i]:
            cnt += 1
        else:
            break
    print(f'#{tc} {cnt}')
