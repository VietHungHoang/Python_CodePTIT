# Cần loại bỏ các kí tự khoảng trắng ở hai đầu chuỗi khi chuyển sang datetime nếu không sẽ lỗi
floor = {'1' : 25, '2' : 34, '3' : 50, '4' : 80}
from datetime import *
class Customer:
    def __init__(self, id, name, roomId, dateIn, dateOut, fee):
        self.id = 'KH{0:0>2}'.format(id)
        self.name = name
        self.roomId = roomId
        self.totaldate = self.getTotalDate(dateIn, dateOut)
        self.pay = self.totaldate * floor[roomId[0]] + fee

    def getTotalDate(self, dateIn, dateOut):
        dIn = datetime.strptime(dateIn, "%d/%m/%Y")
        dOut = datetime.strptime(dateOut, "%d/%m/%Y")
        return (dOut - dIn).days + 1

    def __str__(self):
        return f'{self.id} {self.name} {self.roomId} {self.totaldate} {self.pay}'

if __name__ == '__main__':
    a = []
    for i in range(int(input())):
        a.append(Customer(i + 1, input(), input(), input().strip(), input().strip(), int(input())))
    a.sort(key = lambda x : -x.pay)
    for x in a: print(x)