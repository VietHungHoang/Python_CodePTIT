from math import *

if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        if gcd(int(n), int(n[::-1])) == 1: print("YES")
        else: print("NO")
        