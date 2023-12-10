from math import sqrt
def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 2
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = -1
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in a[i]:
            if isPrime(j) and j > res:
                res = j
    if res == -1:
        print('NOT FOUND')
    else:
        print(res)
        for i in range(n):
            for j in range(m):
                if a[i][j] == res:
                    print('Vi tri [{}][{}]'.format(i, j))
