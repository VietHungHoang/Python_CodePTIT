from math import *
def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        k = 0
        for i in range(1, n):
            if gcd(i, n) == 1: k += 1
        if prime(k): print("YES")
        else: print("NO")