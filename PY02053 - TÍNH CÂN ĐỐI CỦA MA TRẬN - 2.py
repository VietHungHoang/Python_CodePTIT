if __name__ == '__main__':

    n = int(input())
    m = [[]] * n
    for i in range(n):
        m[i] = list(map(int, input().split()))

    sum_up, sum_down = 0, 0
    for i in range(n):
        for j in range(n):
            if j < n - 1 - i:
                sum_up += m[i][j]
            elif j > n - 1 - i:
                sum_down += m[i][j]

    k = int(input())
    sub = abs(sum_up - sum_down)
    print('YES' if sub <= k else 'NO')
    print(sub)
