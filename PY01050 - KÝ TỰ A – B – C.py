
from math import *

def Try(s, a, b, c, n):
    if len(s) == n:
        if a > 0 and a <= b and b <= c: print(s)
    else:   
        Try(s + 'A', a + 1, b, c, n)
        Try(s + 'B', a, b + 1, c, n)
        Try(s + 'C', a, b, c + 1, n)

if __name__ == '__main__':
    for i in range(3, int(input()) + 1):
        Try('', 0, 0, 0, i)
        
        
    