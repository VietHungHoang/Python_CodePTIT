if __name__ == "__main__":
    l = []
    n = int(input())
    for i in range(n):
        l.append(input())
    res = []
    i = 0
    while i < n:
        tmp = len(l[i].split())
        if tmp == 7:
            res.append(2)
            i += 3
        elif tmp == 6:
            if (i < n - 2 and len(l[i + 2].split()) == 7) or i == n - 2:
                res.append(1)
            else: i += 1
        i += 1
    print(len(res))
    for x in res: print(x)
