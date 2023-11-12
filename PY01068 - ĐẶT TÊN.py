n, k = map(int, input().split())
s = sorted(set(input().split()))
n = len(s)
x = [0 for i in range(k + 1)]
def Try(i):
    for j in range(x[i - 1] + 1, n - k + i + 1):
        x[i] = j
        if i == k:
            for t in range(1, k + 1): print(s[x[t] - 1], end = " ")
            print()
        else: Try(i + 1)
if __name__ == "__main__":
    Try(1)