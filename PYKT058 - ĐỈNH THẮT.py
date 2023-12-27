# Nếu tồn tại đường đi từ u tới v mà không đi qua x => x không phải đỉnh thắt
def DFS(n, u, v, x, adj):
    vs = [0] * (n + 1)
    vs[u] = 1
    st = [u]
    while st:
        q = st.pop()
        vs[q] = True
        if q == v: # Tồn tại đường đi từ u đến v mà không đi qua x => x không phải đỉnh thắt
            return False            
        for i in adj[q]:
            if vs[i] == 0 and i != x:
                st.append(i)
    return True

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m, u, v = map(int, input().split())
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input().split())
            adj[x].append(y)
        res = 0
        for i in range(1, n + 1):
            if i != u and i != v:
                res += DFS(n, u, v, i, adj)
        print(res)

