if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        m, M = min(a), max(a)
        print(M - m - len(set(a)) + 1)

