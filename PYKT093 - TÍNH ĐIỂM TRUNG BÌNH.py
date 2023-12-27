from math import *
# Điểm số khi in cần làm tròn lên. Có thể sử dụng 2 cách ở dưới
class Student:
    def __init__(self,id, name, m1, m2, m3):
        self.id = 'SV{0:0>2}'.format(id)
        self.name = " ".join(name.strip().split()).title()
        self.avg = (m1 * 3 + m2 * 3 + m3 * 2) / 8
        self.rank = 0
    def __str__(self):
        return f'{self.id} {self.name} {"%.2f" % (ceil(self.avg * 100) / 100)} {self.rank}'
        # return f'{self.id} {self.name} {"%.2f" % (self.avg + 0.001)} {self.rank}'
if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        l.append(Student(i + 1, input(), int(input()), int(input()), int(input())))
    l.sort(key = lambda x : (-x.avg, x.id))
    l[0].rank = 1
    for i in range(1, n):
        if l[i].avg == l[i - 1].avg:
            l[i].rank = l[i - 1].rank
        else: l[i].rank = i + 1
    print(*l, sep = "\n")