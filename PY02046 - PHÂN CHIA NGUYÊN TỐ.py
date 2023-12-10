def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == "__main__":
    input()
    a = list(map(int, input().split()))
    s = set(a)
    b = []
    for x in a:
        if x in s:
            b.append(x)
            s.discard(x)
    m = len(b)
    sum_b = sum(b)
    cnt = 0
    ok = False
    for i in range(0, m):
        cnt += b[i]
        if prime(cnt) and prime(sum_b - cnt):
            print(i)
            ok = True
            break
    if not ok: print("NOT FOUND")