if __name__ == "__main__":
    d = {}
    n = int(input())
    tmp = []
    for i in range(n):
        s = input()
        if s == "":
            d[tmp[0]] = len(tmp) - 1
            tmp = []
        else:
            tmp.append(s)
        if i == n - 1:
            d[tmp[0]] = len(tmp) - 1
            
    for x in d:
        print(x, d[x], sep = ": ")
