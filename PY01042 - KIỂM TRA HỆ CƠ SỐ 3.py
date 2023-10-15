
def check(n):
    for x in n:
        if x != '0' and x != '1' and x != '2': return False
    return True

if __name__ == '__main__':
    for _ in range(int(input())):
        if check(input()): print("YES")
        else: print("NO")
        
        
        
    