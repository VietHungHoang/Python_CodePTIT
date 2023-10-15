def upNumber(s):
    for i in range(1, len(s)):
            if s[i] < s[i - 1]: return False
    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        if upNumber(input()): print("YES")
        else: print("NO")