#Bài này input có thể đọc trên nhiều dòng nhé
if __name__ == '__main__':
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(x for x in list(map(int, input().split())))
    even, odd = [], []
    for x in a:
        if x % 2 == 0: even.append(x)
        else: odd.append(x)
    i, j = 0, 0
    even.sort()
    odd.sort(reverse = True)
    for x in a:
        if x % 2 == 0: print(even[i], end = " "); i += 1
        else: print(odd[j], end = " "); j += 1