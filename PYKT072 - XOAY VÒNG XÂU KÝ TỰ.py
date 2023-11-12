# Câu này đề sai, nếu không tìm thấy thì in ra -1 chứ không phải in NO
def solve(n, a):
    s = a[0]
    res = 10 ** 9
    for i in range(len(s)):
        cnt = 0
        for j in range(n):
            x = a[j]
            for k in range(len(s)):
                if x == s:
                    cnt += k
                    break
                x = x[1::] + x[0]
            if x != s: return -1 # canot solve
        res = min(res, cnt)
        s = s[1::] + s[0]
    return res


if __name__ == "__main__":
    n = int(input())
    a = [0] * n
    for i in range(n): a[i] = input()
    print(solve(n, a))