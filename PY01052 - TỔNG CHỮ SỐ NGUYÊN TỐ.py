from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == '__main__':
    for t in range(int(input())):
        s = sum(int(i) for i in input())
        print("YES" if prime(s) else "NO")