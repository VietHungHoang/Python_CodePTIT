if __name__ == "__main__":
    a, k, n = map(int, input().split())
    ok = False
    for i in range(1, n//k + 1):
        if i * k - a > 0:
            print(i * k - a, end = " ")
            ok = True
    if not ok: print(-1)