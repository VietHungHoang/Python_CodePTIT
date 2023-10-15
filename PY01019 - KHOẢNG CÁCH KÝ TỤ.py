from math import *
def check(s, t):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(t[i]) - ord(t[i - 1])): return False
    return True

if __name__ == "__main__":
    for i in range(int(input())):
        s = input()
        if check(s, s[::-1]): print("YES")
        else: print("NO")