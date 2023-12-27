from math import isqrt
from array import array as arr
from sys import stdin

maxN = 2000001
prime = arr('i', [0] * maxN)

def sieve():
    for i in range(2, isqrt(maxN) + 1):
        if prime[i] == 0:
            prime[i] = i
            for j in range(i * i, maxN, i):
                prime[j] = i
    for i in range(4, maxN):
        prime[i] += prime[i//prime[i]] if prime[i] else i

if __name__ == '__main__':
    sieve()
    res = 0
    for _ in range(int(stdin.readline())):
        res += prime[int(stdin.readline())]
    print(res)