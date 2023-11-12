class Employee:
    def __init__(self, id, name, mark1, mark2):
        self.id = 'TS0{}'.format(id) ##########
        self.name = name
        if mark1 > 10: mark1 /= 10
        if mark2 > 10: mark2 /= 10
        self.avg = (mark1 + mark2) / 2
    def get_result(self):
        if self.avg > 9.5: return "XUAT SAC"
        elif self.avg >= 8: return "DAT"
        elif self.avg >= 5: return "CAN NHAC"
        else: return "TRUOT"
    def __str__(self):
        return self.id + " " + self.name + " " + f"%.2f" % self.avg + " " + self.get_result() 
if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        l.append(Employee(i + 1, input(), float(input()), float(input())))
    l.sort(key = lambda x : (-x.avg))
    print(*l, sep = '\n')

            