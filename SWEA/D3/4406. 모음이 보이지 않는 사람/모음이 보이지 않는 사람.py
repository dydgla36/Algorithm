aeiou = ['a', 'e', 'i', 'o', 'u']
for tc in range(1, int(input()) + 1):
    st = list(input())
    for i in range(len(st) -1, -1, -1):
        if st[i] in aeiou:
            st.pop(i)
    print(f'#{tc} {"".join(st)}')