if __name__ == "__main__":
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    res = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] > k: res += 1
    print(res + 1)