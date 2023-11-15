repeat1 = "..#."
repeat2 = ".#.#"
repeat3 = "#."
repeat4 = "."
for tc in range(1, int(input()) + 1):
    word = list(map(str, input()))
    print(repeat1 * len(word) + repeat4)
    print(repeat2 * len(word) + repeat4)
    for i in range(len(word)):
        print(repeat3 + word[i] + repeat4, end="")
        if i == len(word) - 1:
            print('#')
    print(repeat2 * len(word) + repeat4)
    print(repeat1 * len(word) + repeat4)
