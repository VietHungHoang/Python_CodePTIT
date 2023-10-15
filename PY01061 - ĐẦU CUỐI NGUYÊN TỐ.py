from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        print("YES" if prime(int(s[0:3])) and prime(int(s[-3:])) else "NO")