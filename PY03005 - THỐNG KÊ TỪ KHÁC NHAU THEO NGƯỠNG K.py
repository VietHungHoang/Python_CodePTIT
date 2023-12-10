if __name__ == '__main__':
    d = {}
    n, k = map(int, input().split())
    for _ in range(n):
        s = input().lower()
        for x in s:
            if not (x.isdigit() or x.isalpha()): s = s.replace(x, ' ')
        for j in s.split():
            if j in d: d[j] += 1
            else: d[j] = 1
    for x in sorted(d.items(), key=lambda x: (-x[1], x[0])):
        if x[1] >= k: print(x[0], x[1])