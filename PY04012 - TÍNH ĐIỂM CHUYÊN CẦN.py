import collections


class Student:
    def __init__(self, id, name, className):
        self.id = id
        self.name = name
        self.className = className
        self.mark = 10
        self.note = ""
    def __str__(self):
        return f'{self.id} {self.name} {self.className} {self.mark} {self.note}'
if __name__ == '__main__':
    n = int(input())
    d = {}
    for _ in range(n):
        id = input()
        name = input()
        className = input()
        d[id] = Student(id, name, className)
    for _ in range(n):
        id, s = input().split()
        for x in s:
            if x == 'm': d[id].mark -= 1
            elif x == 'v': d[id].mark -= 2
        if d[id].mark <= 0:
            d[id].mark = 0
            d[id].note = 'KDDK'
    for x in d: print(d[x])