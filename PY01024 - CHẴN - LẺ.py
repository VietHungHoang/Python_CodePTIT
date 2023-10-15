from math import *

def sumDigit(n):
    res = 0
    for x in n: res += int(x)
    return res

def check(s):
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2: return False
    return sumDigit(s) % 10 == 0

if __name__ == "__main__":
    for i in range(int(input())):
        if check(input()): print("YES")
        else: print("NO")