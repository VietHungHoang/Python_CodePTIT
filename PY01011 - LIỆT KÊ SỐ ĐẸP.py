a = []

def checkRev(n):
    for i in n:
        if int(i) % 2 == 1: return False
    return n == n[::-1] and len(n) % 2 == 0

for i in range(22, 1000001):
    if checkRev(str(i)): a.append(i)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        for x in a:
            if x <= n: print(x, end = " ")
            else: break
        print()
