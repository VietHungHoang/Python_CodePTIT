if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        s = input()
        i = 0
        while i < len(s):
            if s[i].isdigit():
                idx = i
                while i < len(s) and s[i].isdigit(): i += 1
                l.append(int(s[idx:i]))
                i -= 1
            i += 1
    for x in sorted(l): print(x)