m = []

def check(n):
    for x in n:
        if int(x) % 2 != 0: return False    
    return len(n) % 2 == 0 and n == n[::-1]

if __name__ == '__main__':
    for i in range(22, 1000001):
        if check(str(i)): m.append(i)
    for _ in range(int(input())):
        n = int(input())
        for x in m:
            if x < n: print(x, end = " ")
            else: break
        print()
        
        
        
    