if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a, b, c = [], [], list(map(int, input().split()))
        for x in c:
            if x < 0:
                a.append(x)
            else:
                b.append(x)
        c = a + b
        c.insert(c.index(max(c)), m)
        print(*c, sep = " ")