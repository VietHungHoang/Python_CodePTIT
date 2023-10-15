
def check(n):
    for i in range(0, len(n), 2):
        if n[i] != n[0]: return False
    for i in range(1, len(n), 2):
        if n[i] != n[1]: return False
    return True

if __name__ == '__main__':
    for _ in range(int(input())):
        if check(input()): print("YES")
        else: print("NO")
        
        
    