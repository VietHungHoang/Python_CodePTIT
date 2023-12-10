#Ý tưởng: Với mỗi bước có thể tăng hoặc giảm giá trị của một số chưa nguyên tố => Tìm số bước để biến các số thành số nguyên tố. Kết quả chính là giá trị lớn nhất
# Cài đặt: Sử dụng sàng số nguyên tố biến đổi để liệt kê các số nguyên tố nhỏ hơn 100001

# Sàng số nguyên tố biến đổi
p = [1] * 10001
b = [] # lưu danh sách các số nguyên tố theo thứ tự từ nhỏ đến lớn
p[0] = p[1] = 0
for i in range(2, 10001):
    if p[i] == 1:
        for j in range(i * i, 10001, i):
            p[j] = 0
        b.append(i)
if __name__ == "__main__":
    n = input()
    ans = 0
    c = map(int, input().split())
    for i in c:
        s = 10**9
        for j in b:
            # Với mỗi số trong mảng, tìm số bước ít nhất để biến số đó thành số nguyên tố
            s = min(s, abs(i - j))
        # Số bước ít nhất để biến mảng đó thành mảng nguyên tố là số bước để biến phần tử có s_max thành số nguyên tố
        ans = max(ans, s)
    print(ans)