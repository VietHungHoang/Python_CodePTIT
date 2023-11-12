dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    q = []
    res = 0
    for i in range(n):
        a.append(list(map(int, input().split())))
        for j in range(m):
            if a[i][j] == -1:
                q.append([i,j])
    while len(q) > 0:
        u = q[0]
        q.pop(0)
        for k in range(8):
            i1, j1 = u[0] + dy[k], u[1] + dx[k]
            if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m and a[i1][j1]:
                res += a[i1][j1]
                a[i1][j1] = 0
    print(res)


