if __name__ == "__main__":
    n = int(input())
    a = [input() for _ in range(n)]
    res = 0
    for x in a:
        tmp = x.count('C')
        res += tmp * (tmp - 1) // 2
    for i in range(n):
        s = [a[j][i] for j in range(n)]
        tmp = s.count('C')
        res += tmp * (tmp - 1) // 2
    print(res)