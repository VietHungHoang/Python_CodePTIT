# Ý tưởng: Sử dụng tham lam
# Dễ thấy giá trị idx = a[i]/b[i] nằm trong đoan [1, min(a[i])].
# Mỗi bước duyệt các số trong đoạn [1, min(a[i])]. Rồi tìm giá trị nhỏ nhất có thể của b[i].
# Trong trường hợp không tìm được b[i] thoả mãn a[i] / b[i] = idx => bỏ qua trường hợp đó.
if __name__ == '__main__':
    input()
    a = list(map(int, input().split()))
    val = min(a)
    res = 10**9
    for i in range(1, val + 1):
        cnt = 0
        for x in a:
            tmp = x // i
            if x // tmp != i:
                cnt = 10**9
                break
            while tmp > 0 and x // tmp == i:
                tmp -= 1
            cnt += tmp + 1
        res = min(res, cnt)
    print(res)
