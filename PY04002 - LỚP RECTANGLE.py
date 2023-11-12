class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color.title()
    
    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.width > 0 and r.height > 0:
    print(r.perimeter(), r.area(), r.color)
else: print("INVALID")

# Code PTIT lỗi, bỏ hàm main đi thì mới AC
# 25/10/2023