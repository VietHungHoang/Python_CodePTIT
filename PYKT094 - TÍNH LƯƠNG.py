class Room:
    def __init__(self, inp):
        a = inp.split()
        self.id = a[0]
        self.name = " ".join(a[1:])
class Employee:
   def __init__(self, id, name, basicSalary, workDay):
       self.id = id
       self.name = name
       self.totalSalary = self.calTotalSalary(basicSalary, workDay)
   def calTotalSalary(self, basicSalary, workDay):
        mul = 0
        if self.id.startswith('A'):
            if int(self.id[1:3]) > 16: mul = 20
            elif int(self.id[1:3]) >= 9: mul = 14
            elif int(self.id[1:3]) >= 4: mul = 12
            else: mul = 10
        elif self.id.startswith('B'):
            if int(self.id[1:3]) > 16: mul = 16
            elif int(self.id[1:3]) >= 9: mul = 13
            elif int(self.id[1:3]) >= 4: mul = 11
            else: mul = 10
        elif self.id.startswith('C'):
            if int(self.id[1:3]) > 16: mul = 14
            elif int(self.id[1:3]) >= 9: mul = 12
            elif int(self.id[1:3]) >= 4: mul = 10
            else: mul = 0
        elif self.id.startswith('D'):
            if int(self.id[1:3]) > 16: mul = 13
            elif int(self.id[1:3]) >= 9: mul = 11
            elif int(self.id[1:3]) >= 4: mul = 9
            else: mul = 8
        return basicSalary * mul * workDay * 1000
   def __str__(self):
       return f'{self.id} {self.name} {self.room.name} {self.totalSalary}'

if __name__ == '__main__':
    l = []
    rooms = {}
    for i in range(int(input())):
        tmp = Room(input())
        rooms[tmp.id] = tmp
    n = int(input())
    for i in range(n):
        l.append(Employee(input(), input(), int(input()), int(input())))
        l[i].room = rooms[l[i].id[3:]]
    for x in l: print(x)
