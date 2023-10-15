for _ in range(int(input())):
    n = int(input())
    ok = False
    for i in range(1000):
        if n % 7 == 0:
            print(n)
            ok = True
            break
        n = n + int("".join(reversed(str(n))))
    if not ok: print(-1)
    
    