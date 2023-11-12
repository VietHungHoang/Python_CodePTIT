if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        res = 0
        t = ""
        for i in s:
            if i.isdigit(): res += int(i)
            else: t += i
        print(*sorted(t), res, sep = "")

