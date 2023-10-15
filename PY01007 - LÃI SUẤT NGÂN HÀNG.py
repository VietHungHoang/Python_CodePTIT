from math import *
for i in range(int(input())):
     n, x, m = map(float, input().split())
     print(ceil(log(m / n, 1 + x/100)))
