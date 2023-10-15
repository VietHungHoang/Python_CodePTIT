from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

list = [0, 2]
x = 3
while len(list) <= 1001:
    if isPrime(x): list += [x]
    x += 2
    
if __name__ == '__main__':

    n, x = map(int, input().split())
    for i in range(n + 1):
        x += list[i]
        print(x, end = ' ')
