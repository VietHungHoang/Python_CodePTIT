n = None
a = [0] * 15
l = []
def Try(i,cnt):
    global a, n
    for j in range(n, 0, -1):
        if cnt - j >= 0 and (i == 0 or (i > 0 and j <= a[i - 1])):
            a[i] = j
            if cnt - j == 0:
                res = "("
                for k in range(i):
                    res += str(a[k]) + " "
                res += str(a[i]) + ")"
                l.append(res)
            else: Try(i + 1, cnt - j)
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        l = []
        Try(0, n)
        print(len(l))
        print(*l)
