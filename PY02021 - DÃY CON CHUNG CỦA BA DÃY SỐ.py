from collections import defaultdict
if __name__ == '__main__':
    for _ in range(int(input())):
        a = input()
        d1 = defaultdict(int)
        for x in input().split(): d1[x] += 1
        d2 = defaultdict(int)
        for x in input().split(): d2[x] += 1
        d3 = defaultdict(int)
        for x in input().split(): d3[x] += 1
        ok = False
        for x in d1:
            if d2[x] > 0 and d3[x] > 0:
                print(*([x] * min(d1[x], d2[x], d3[x])), end = ' ')
                ok = True
        if not ok: print("NO")
        else: print()