import collections
if __name__ == "__main__":
    s = input()
    l = []
    d = collections.defaultdict(int)
    for i in range(0, len(s), 2):
        tmp = int(s[i:i + 2])
        if tmp > 9:
            if tmp not in d: l.append(tmp)
            d[tmp] += 1
    for x in l:
        print(x, d[x])