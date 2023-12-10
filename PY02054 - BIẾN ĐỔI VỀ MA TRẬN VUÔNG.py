if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    if n > m:
        tmp = n - m
        while tmp:
            a.pop(2*(tmp - 1))
            tmp -= 1
    elif m > n:
        tmp = m - n
        2 * (tmp - 1) + 1
        while tmp:
            for x in a: x.pop(2 * (tmp - 1) + 1)
            tmp -= 1
    for x in a: print(*x)