from math import *

def analysis(n):
    print("1", end = '')
    for i in range(2, isqrt(n) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt > 0: print(" * ", i, '^', cnt, sep = '', end = '')
    if n > 1: print(" * ", n, '^', 1, sep = '', end = '')

if __name__ == "__main__":
    for i in range(int(input())):
        analysis(int(input()))
        print()
        