def cal(s):
    if s[3] == "OUT": return 0
    if s[1] == "Xe_con":
        return 10000 if s[2] == "5" else 15000
    elif s[1] == "Xe_tai": return 20000
    elif s[2] == "29": return 50000
    else: return 70000

if __name__ == "__main__":
    d = {}
    n = int(input())
    for _ in range(n):
        s = input().split()
        if s[-1] in d: d[s[-1]] += cal(s)
        else: d[s[-1]] = cal(s)
    for x in d: print(f"{x}: {d[x]}")
