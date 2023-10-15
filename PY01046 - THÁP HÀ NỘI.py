
def HanoiTower(n, a, b, c):
    if n == 1: print(a + " -> " + c)
    else:
        HanoiTower(n - 1, a, c, b)
        HanoiTower(1, a, b, c)
        HanoiTower(n - 1, b, a, c)

if __name__ == '__main__':
    HanoiTower(int(input()), 'A', 'B', 'C')
        
        
        
    