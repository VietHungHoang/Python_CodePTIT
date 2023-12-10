from math import *
def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1


if __name__ == "__main__":
    input()
    a = list(map(int, input().split()))
    p = []
    for x in a:
        if prime(x): p.append(x)
    p.sort()
    i = 0
    for x in a:
        if x in p:
            print(p[i], end = ' ')
            i += 1
        else: print(x, end = ' ')
