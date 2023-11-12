if __name__ == '__main__':
    n = int(input())
    a = [[]] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))

    sum_up, sum_down = 0, 0
    for i in range(n):
        for j in range(n):
            if i < j: sum_down += a[i][j]
            elif i > j: sum_up += a[i][j]
    k = int(input())
    sub = abs(sum_up - sum_down)
    print('YES' if sub <= k else 'NO')
    print(sub)
