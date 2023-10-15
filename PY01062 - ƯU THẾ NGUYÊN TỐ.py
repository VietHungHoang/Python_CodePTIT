from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        cnt = 0
        for i in s:
            if prime(int(i)): cnt += 1
        print("YES" if prime(len(s)) and cnt > len(s) - cnt else "NO")