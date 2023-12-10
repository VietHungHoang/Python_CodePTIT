if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = [0] * (m + 1)
    for x in map(int, input().split()):
        cnt[x] += 1
    max_n = max(cnt)
    for i in range(m + 1):
        if cnt[i] == max_n: cnt[i] = 0
    if len(set(cnt)) == 1: print("NONE")
    else:
        max_n = cnt[1]
        res = 0
        for i in range(m + 1):
            if cnt[i] > max_n:
                res = i
                max_n = cnt[i]
        print(res)
