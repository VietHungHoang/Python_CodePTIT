if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        a = map(int, input().split())
        cnt = [0] * 1000001
        for x in a: cnt[x] += 1
        for i in range(1000001):
            if cnt[x] % 2 != 0: print(x); break