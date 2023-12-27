from  datetime import datetime
t = {}

class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class Schedule:
    def __init__(self, id, subject, date, time, group):
        self.id = 'T{0:0>3}'.format(id)
        self.subject = subject
        self.date = date + " " + time
        self.group = group

    def __str__(self):
        return f'{self.id} {self.subject.id} {self.subject.name} {self.date} {self.group}'

if __name__ == '__main__':
    n, m = map(int, input().split())
    subjects = {}
    for i in range(n):
        tmp = Subject(input(), input())
        subjects[tmp.id] = tmp
    l = []
    for i in range(m):
        tmp = input().split()
        l.append(Schedule(i + 1, subjects[tmp[0]], tmp[1], tmp[2], tmp[3]))
    for x in sorted(l, key = lambda x : (datetime.strptime(x.date, "%d/%m/%Y %H:%M"), x.id)):
        print(x)