from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return sqrt(pow(self.x - point.x, 2) + pow(self.y - point.y, 2))

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        return "INVALID" if max(a, b, c) * 2 >= a + b + c else f"{a + b + c:.3f}"

    def __str__(self):
        return self.perimeter()

if __name__ == '__main__':
    l = []
    i = 0
    for _ in range(int(input())):
        l += list(map(float, input().split()))
        A = Point(l[i + 0], l[i + 1])
        B = Point(l[i + 2], l[i + 3])
        C = Point(l[i + 4], l[i + 5])
        print(Triangle(A, B, C))
        i += 6

# bài này phải nhập hết test rồi in thì mới AC, nhập đến đâu in đến đấy như bình thường thì bị WA