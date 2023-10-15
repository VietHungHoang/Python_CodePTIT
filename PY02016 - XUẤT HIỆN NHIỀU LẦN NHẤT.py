if __name__ == '__main__':
    for _ in range(int(input())):
        cnt = [0] * 1000001
        n = int(input())
        a = list(map(int, input().split()))
        M, m = 0, 10**18
        for x in a:
            cnt[x] += 1
            M = max(x, M)
            m = min(x, m)
        res = 1
        for i in range(m, M + 1):
            if cnt[i] > cnt[res]: res = i
        if cnt[res] > n//2: print(res)
        else: print("NO")