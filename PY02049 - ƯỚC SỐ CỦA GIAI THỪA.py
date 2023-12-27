# Ý tưởng: Duyệt các bội của 7 trong n!
if __name__ == '__main__':
    for _ in range(int(input())):
        n, p = map(int, input().split())
        x,res = 1, 0
        while n / (p**x) > 1:
            res += n // (p**x)
            x += 1
        print(res)

# Cách khác:
#     for t in range(int(input())):
#         n, p = map(int, input().split())
#         x = 0
#         for i in range(2, n + 1):
#             num = i
#             while num % p == 0:
#                 num /= p
#                 x += 1
#         print(x)
