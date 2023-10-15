if __name__ == "__main__":
    for i in range(int(input())):
        s = input()
        if s[len(s) - 2] == '8' and s[len(s) - 1] == '6': print("YES")
        else: print("NO")