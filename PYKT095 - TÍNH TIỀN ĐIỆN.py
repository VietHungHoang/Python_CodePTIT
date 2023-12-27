t = {'A' : 100, 'B' : 500, 'C' : 200}
class Customer:
    def __init__(self, id, name, type, start, end):
        self.id = 'KH{:02d}'.format(id)
        self.name = " ".join(name.strip().split()).title()
        self.calMoney(type, int(start), int(end))

    def calMoney(self, type, start, end):
        num = end - start
        out = num - t[type]
        if out >= 0:
            self.moneyIn = t[type] * 450
            self.moneyOut = out * 1000
        else:
            self.moneyIn = num * 450
            self.moneyOut = 0
        self.vat = self.moneyOut // 20
        self.totalMoney = self.moneyIn + self.moneyOut + self.vat
    def __str__(self):
        return f'{self.id} {self.name} {self.moneyIn} {self.moneyOut} {self.vat} {self.totalMoney}'
if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        l.append(Customer(i + 1, input(), *input().split()))
    l.sort(key = lambda x : -x.totalMoney)
    print(*l, sep = '\n')