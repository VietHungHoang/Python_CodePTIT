if __name__ == "__main__":
    s = input()
    l = []
    for i in range(0, len(s), 2):
        tmp = int(s[i:i + 2])
        if tmp > 9: l.append(tmp)
    st = set(l)
    for x in l:
        if x in st:
            print(x, end = ' ')
            st.discard(x)
