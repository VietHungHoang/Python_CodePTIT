if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        n = input()
        res, idx = 0, s.find(n)
        while idx != -1:
            res += 1
            idx = s.find(n, idx + len(n))
        print(res)
        