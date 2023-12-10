if __name__ == "__main__":
    n, m = map(int, input().split())
    res = -1
    max_val, min_val = -1, 10**9
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        max_val = max(max(a[i]), max_val)
        min_val = min(min(a[i]), min_val)
    for i in range(n):
        for j in a[i]:
            if j == max_val - min_val:
                res = j
    if res == -1:
        print('NOT FOUND')
    else:
        print(res)
        for i in range(n):
            for j in range(m):
                if a[i][j] == res:
                    print('Vi tri [{}][{}]'.format(i, j))
