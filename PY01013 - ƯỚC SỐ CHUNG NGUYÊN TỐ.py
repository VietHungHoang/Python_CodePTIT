from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

def sumDigit(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res
if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if prime(sumDigit(gcd(a, b))): print("YES")
        else: print("NO")
    