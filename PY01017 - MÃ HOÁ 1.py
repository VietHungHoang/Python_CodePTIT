if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        st = 0
        for i in range(1, len(s)):
            if s[i] != s[st]:
                print(i - st, s[st], sep = '', end = '')
                st = i
        print(len(s) - st, s[st], sep = '')