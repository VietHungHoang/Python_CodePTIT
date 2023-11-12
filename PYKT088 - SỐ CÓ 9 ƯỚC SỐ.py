# Một số có đúng 9 ước số khi nó là bình phương của tích hai số nguyên tố hoặc là p^8 với p là số nguyên tố
if __name__ == "__main__":
    n = int(input())
    m = int(n ** 0.5)
    res = 0
    prime = [x for x in range(m + 1)]
    for i in range(2, int(m ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, m + 1, i):
                if prime[j] == j:
                    prime[j] = i
    for i in range(2, m + 1):
        a = prime[i]
        b = prime[i // a]
        if a * b == i and a != b and b != 1: res += 1
        elif prime[i] == i and i ** 8 <= n: res += 1
    print(res)

