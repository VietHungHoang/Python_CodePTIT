import bisect

N = 10 ** 18
hamming = []
# init
i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            hamming.append(i * j * k)
            k *= 5
        j *= 3
    i *= 2
hamming.sort()

if __name__ == '__main__':
    for _ in range(int(input())):
        x = int(input())
        tmp = bisect.bisect_left(hamming, x)
        if tmp != len(hamming) and hamming[tmp] == x: print(tmp + 1)
        else: print("Not in sequence")
    