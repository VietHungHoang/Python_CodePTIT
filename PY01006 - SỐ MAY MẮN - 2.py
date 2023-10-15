def luckyNumber(n):
    for i in n:
        if i != '4' and i != '7': return False
    return True
if __name__ == '__main__':
    for t in range(int(input())):
        if luckyNumber(input()): print("YES")
        else: print("NO")