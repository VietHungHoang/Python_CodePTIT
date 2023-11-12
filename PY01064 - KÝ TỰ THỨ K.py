if __name__ == "__main__": 
    for _ in range(int(input())):
        n, k = map(int, input().split())
        while n:
            tmp = 2 ** (n - 1)
            if k == tmp:
                print(chr(64 + n))
                break
            n -= 1
            if k > tmp: k -= tmp
