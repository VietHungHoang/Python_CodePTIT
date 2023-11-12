if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = sorted(list(map(int, input().split())))
        res = 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                tmp = a[i] + a[l] + a[r]
                if not tmp:
                    res += 1
                    l += 1
                elif tmp < 0: l += 1
                else: r -= 1
        print(res)

        
