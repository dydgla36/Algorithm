for tc in range(1, int(input()) + 1):
    st = list(input())
    tree = [1,1]
    for i in st:
        if i == 'L':
            tree[1] += tree[0]
        else:
            tree[0] += tree[1]
    print(f'#{tc} {" ".join(map(str, tree))}')