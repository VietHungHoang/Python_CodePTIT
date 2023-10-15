
from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        if prime(int(s[len(s) - 4:])): print("YES")
        else: print("NO")
        
        
    