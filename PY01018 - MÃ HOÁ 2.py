if __name__ == "__main__":
    while True:
        s = input()
        if s == '0': break
        else:
            p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
            a, b = s.split()
            a = int(a)
            for i in range(len(b)):
                b[i] == b.find(i)
            for x in b[::-1]: print(x, end = '')
            print()