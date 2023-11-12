if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        res = ""
        while n:
            tmp = n % k
            if tmp < 10: res = str(tmp) + res
            else: res = str(chr(tmp + 55)) + res
            n //= k
        print(res)