from collections import  defaultdict
if __name__ == '__main__':
    file = open('VANBAN.in', 'r')
    d = defaultdict(int)
    max_len = -1
    for line in file:
        for x in line.split():
            if x[::-1] == x:
                d[x] += 1
                max_len = max(max_len, len(x))
    for x in d:
        if len(x) == max_len: print(x, d[x])