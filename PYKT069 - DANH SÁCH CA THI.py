from  datetime import datetime
class Exam:
    def __init__(self,id, date, time, room):
        self.id = 'C{0:0>3}'.format(id)
        self.date = date
        self.time = time
        self.room = room

    def __str__(self):
        return f'{self.id} {self.date} {self.time} {self.room}'

if __name__ == '__main__':
    file = open("CONTACT.in", 'r')
    n = int(file.readline().rstrip())
    a = []
    for i in range(n): a.append(Exam(i + 1, file.readline().rstrip(), file.readline().rstrip(), file.readline().rstrip()))
    a.sort(key=lambda x: (datetime.strptime(x.date + ' ' + x.time, "%d/%m/%Y %H:%M"), x.id))
    for x in a: print(x)

