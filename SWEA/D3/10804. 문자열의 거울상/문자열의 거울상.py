r_word = {"b" : "d", "d" : "b", "p" : "q", "q" : "p"}
for tc in range(1, int(input()) + 1):
    word = list(map(str, input()))
    result = []
    for i in range(len(word) - 1, -1, -1):
        if word[i] in r_word:
            result.append(r_word[word[i]])
    print(f'#{tc} {"".join(result)}')
