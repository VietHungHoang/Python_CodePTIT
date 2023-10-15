from math import *

def check(s):
    for i in range(len(s)):
        if i % 2 != int(s[i]) % 2:
            return False
        
    n = sum(int(i) for i in s)
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    for t in range(int(input())):
        print("YES" if check(input()) else "NO")
