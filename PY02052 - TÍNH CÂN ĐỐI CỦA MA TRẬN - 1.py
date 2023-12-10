if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    up, down = 0, 0
    for i in range(n):
        for j in range(n):
            if j < i: down += a[i][j]
            elif j > i: up += a[i][j]
    print("YES" if abs(up - down) <= k else "NO")
    print(abs(up - down))