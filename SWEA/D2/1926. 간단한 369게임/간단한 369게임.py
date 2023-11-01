n = int(input())
for i in range(1, n + 1):
    st = str(i)
    count = st.count("3") + st.count("6") + st.count("9") 
    if count > 0:
        print(count * "-", end = " ")
    else:
        print(st, end=" ")
