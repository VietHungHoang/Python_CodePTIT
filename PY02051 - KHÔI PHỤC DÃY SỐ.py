if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    if n == 2: print(a[1] // 2, a[1] // 2)
    else:
        for i in range(n):
            try:
                print((a[i][i - 1] + a[i][i + 1] - a[i - 1][i + 1]) // 2, end = ' ')
            except: #số cuối cùng
                print((a[i][i - 1] + a[i][0] - a[i - 1][0]) // 2, end=' ')

