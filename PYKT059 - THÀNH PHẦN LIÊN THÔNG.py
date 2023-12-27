def DFS(n, u, adj):
    vs = [0] * (n + 1)
    vs[u] = 1
    st = [u]
    while st:
        q = st.pop()
        vs[q] = True
        for i in adj[q]:
            if vs[i] == 0:
                st.append(i)
    ok = False
    for i in range(1, n + 1):
        if vs[i] == 0:
            ok = True
            print(i)
    if not ok: print(0)

if __name__ == '__main__':
        n, m, u = map(int, input().split())
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input().split())
            adj[x].append(y)
            adj[y].append(x)
        DFS(n, u, adj)

