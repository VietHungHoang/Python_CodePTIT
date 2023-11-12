def check(n, u, v, k, adj):
    # use BFS
    q = [u] # push u to queue
    vs = [0] * (n + 1)# visited q
    vs[u] = 1
    while len(q):
        x = q.pop()
        if x == v: return False
        for i in adj[x]:
            if not vs[i] and i != k:
                q.append(i)
                vs[i] = 1
    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, u, v = map(int, input().split())
        adj = [[] for i in range(n + 1)]
        for j in range(m):
            x, y = map(int, input().split())
            adj[x].append(y)
        res = 0
        for i in range(n + 1):
            if i != u and i != v:
                res += check(n, u, v, i, adj) # nếu i không tồn tại thì có đường đi từ u đến v ko
        print(res)