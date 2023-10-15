
from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

def check(n):
    cnt = 0
    for x in n:
        if prime(int(x)): cnt += 1
    return cnt > len(n) - cnt and prime(len(n))

if __name__ == '__main__':
    for _ in range(int(input())):
        if check(input()): print("YES")
        else: print("NO")
        
        
    