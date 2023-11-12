if __name__ == "__main__":
    for _ in range(int(input())):
        s = input().split()
        tmp = ""
        for x in s:
            if len(tmp) + len(x) + 1 <= 101:
                tmp += x + " "
            else: break
        print(tmp)