def trans(s):
    n = 0
    for i in s : n += ord(i) - 48
    return str(n)

if __name__ == "__main__":
    s = input()
    res = 0
    while len(s) > 1:
        s = trans(s)
        res += 1
    print(res)