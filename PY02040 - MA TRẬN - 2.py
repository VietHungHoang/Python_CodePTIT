if __name__ == '__main__':
    n = int(input())
    a = [[]] * n
    for i in range(n): a[i] = list(map(int, input().split()))

    sum_up, sum_down = 0, 0
    for i in range(n):
        for j in range(n):
            if j < n - i - 1: sum_up += a[i][j]
            elif j > n - i - 1: sum_down += a[i][j]

    k = int(input())
    sub = abs(sum_up - sum_down)
    print('YES' if sub <= k else 'NO')
    print(sub)
