if __name__ == "__main__":
    n = int(input())
    l = []
    while True:
        l += list(map(int, input().split()))
        if len(l) == n: break
    ok = False
    for i in range(1, l[-1] + 1):
        if i not in l:
            print(i)
            ok = True
    if not ok: print("Excellent!")
