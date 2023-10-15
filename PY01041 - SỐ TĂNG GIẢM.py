
def check(n):
    sz = len(n) - 1
    if len(n) < 3: return False
    i = 0
    while i < sz and n[i] < n[i + 1]: i += 1
    if i == sz: return False
    else:
        while i < sz and n[i] > n[i + 1]: i += 1
        if i == sz: return True
        else: return False

if __name__ == '__main__':
    for _ in range(int(input())):
        if check(input()): print("YES")
        else: print("NO")
        
        
        
    