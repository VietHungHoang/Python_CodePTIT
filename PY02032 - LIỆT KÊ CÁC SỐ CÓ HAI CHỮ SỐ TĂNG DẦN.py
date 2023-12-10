if __name__ == "__main__":
    s = input()
    st = set()
    for i in range(0, len(s), 2):
        tmp = int(s[i:i + 2])
        if tmp > 9: st.add(tmp)
    print(*sorted(st))
