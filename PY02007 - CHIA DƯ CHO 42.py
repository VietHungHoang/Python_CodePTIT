if __name__ == '__main__':
    s = set()
    cnt = 10
    while cnt != 0:
        a = list(map(int, input().split()))
        cnt -= len(a)
        for x in a: s.add(x % 42)
    print(len(s))

    