# Đồ thị là đồ thị hình sao khi có một đỉnh kề với tất cả các đỉnh còn lại còn tất cả các đỉnh còn lại chỉ có duy nhất một đỉnh kề
# Ý tưởng: Đếm số đỉnh kề của tất cả các đỉnh rồi kiểm tra.
# Để nhanh hơn, có thể thấy rằng đồ thị là hình sao khi tất cả các đỉnh, số lượng đỉnh kề với nó là 1 hoặc n - 1.
from collections import defaultdict
if __name__ == '__main__':
    d = defaultdict(int)
    n = int(input())
    for i in range(n - 1):
        x, y = map(int, input().split())
        d[x] += 1
        d[y] += 1
    ok = True
    for i in range(1, n + 1):
        if d[i] != 1 and d[i] != n - 1:
            ok = False
            break
    print("Yes" if ok else "No")