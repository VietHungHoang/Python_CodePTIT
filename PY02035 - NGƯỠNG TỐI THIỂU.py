import collections

if __name__ == "__main__":
    s = input()
    n = int(input())
    d = collections.defaultdict(int)
    for i in range(0, len(s), 2):
        tmp = int(s[i:i + 2])
        if tmp > 9:
            d[tmp] += 1
    ok = False
    for x, y in (sorted(d.items(), key = lambda x : x[0])):
        if y >= n:
            ok = True
            print(x, y)
    if not ok: print("NOT FOUND")