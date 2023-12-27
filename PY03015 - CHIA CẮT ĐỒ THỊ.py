def DFS(n, adj, u, k):
    global vs
    vs[u] = 1
    st = [u]
    while st:
        q = st.pop()
        vs[q] = True
        for i in adj[q]:
            if vs[i] == 0 and i != k:
                st.append(i)

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int,input().split())
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input().split())
            adj[x].append(y)
            adj[y].append(x)
        vs = [0] * (n + 1)
        res = 0
        for i in range(1, n + 1):
            if not vs[i]:
                DFS(n, adj, i, 0)
                res += 1
        v = 0
        for i in range(1, n + 1):
            vs = [0] * (n + 1)
            cnt = 0
            for j in range(1, n + 1):
                if i != j and not vs[j]:
                    DFS(n, adj, j, i)
                    cnt += 1
            if cnt > res:
                res = cnt
                v = i
        print(v)