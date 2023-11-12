maxN = int(1e6+1)

prime = [1] * maxN
prime[0] = prime[1] = 0
for i in range(1000):
    if prime[i]:
        for j in range(i*i, maxN, i):
            prime[j] = 0
if __name__ == '__main__':
    for _ in range(int(input())):
        used = []
        n = int(input())
        for i in range(2, n):
            s = str(i)
            t = s[::-1]
            if s != t and int(t) < n and prime[i] and prime[int(t)] and s not in used:
                print(s, t, end = " ")
                used.append(s)
                used.append(t)
        print()