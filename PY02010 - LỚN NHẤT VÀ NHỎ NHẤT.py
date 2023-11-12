if __name__ == "__main__": 
    while True:
        n = int(input())
        if not n: break
        a = []
        for _ in range(n):
            a.append(int(input()))
        a.sort()
        if a[0] == a[-1]: print("BANG NHAU")
        else: print(a[0], a[-1])