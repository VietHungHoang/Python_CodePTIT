if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        q = ['1', '2']
        while n:
            a = str(int(q.pop(0)))
            if a.count('2') > len(a) / 2:
                n -= 1
                print(a, end = ' ')
            q.append(a + '0')
            q.append(a + '1')
            q.append(a + '2')
        print()