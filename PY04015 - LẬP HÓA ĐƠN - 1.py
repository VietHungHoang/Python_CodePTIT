class Customer:
    def __init__(self, id, name, old, new):
        self.id = f"KH{id:02d}"
        self.name = name
        self.used = new - old
    def getPrice(self):
        if self.used > 100:
            return round(((self.used - 100) * 200 + 50 * 150 + 50 * 100)* 1.05)
        elif self.used > 50:
            return round(((self.used - 50) * 150 + 50 * 100) * 1.03)
        else: return round(self.used * 100 * 1.02)
    def __str__(self):
        return self.id + " " + self.name + " " + str(self.getPrice())
if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        l.append(Customer(i + 1, input(), int(input()), int(input())))
    l.sort(key = lambda x : (-x.getPrice()))
    for x in l: print(x)

