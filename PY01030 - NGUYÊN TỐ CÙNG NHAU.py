from math import *

if __name__ == "__main__":
    n, k = map(int, input().split())
    cnt = 0
    for i in range(10 ** (k - 1), 10 ** k, 1):
        if gcd(n, i) == 1:
            print(i, end = ' ')
            cnt += 1
        if cnt == 10:
            cnt = 0; print()