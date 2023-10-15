def Try(i):
    global n, k
    for j in range(i, n):
        if (i > 0 and a[j] > x[i - 1]) or i == 0:
            x[i] = a[j]
            if i == k - 1: print(*x)
            else: Try(i + 1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = sorted(list({int(i) for i in input().split()}))
    n = len(a)
    x = [0] * k
    Try(0)
    