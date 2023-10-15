from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == '__main__':

    n = int(input())
    a = map(int, input().split())
    m = {}
    for i in a:
        if isPrime(i):
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
    for i in m: print(i, m[i])
