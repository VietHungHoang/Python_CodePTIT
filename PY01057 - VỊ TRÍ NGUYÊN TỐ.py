from math import *

def prime(n):
    return n == 2 or n == 3 or n == 5 or n == 7

def check(s):
    for i in range(len(s)):
        if (prime(i) and not prime(int(s[i]))) or (not prime(i) and prime(int(s[i]))):
            return False
    return True

if __name__ == '__main__':
    for t in range(int(input())):
        print("YES" if check(input()) else "NO")