from  datetime import datetime
class Subject:
    def __init__(self, id, name, exam_format):
        self.id = id
        self.name = name
        self.exam_format = exam_format

class Session:
    def __init__(self, id, date, time, room):
        self.id = 'C{0:0>3}'.format(id)
        self.date = date
        self.time = time
        self.room = room

class Schedule:
    def __init__(self, session, subject, group_id, nos):
        self.subject = subject
        self.session = session
        self.group_id = group_id
        self.nos = nos

    def __str__(self):
        return f'{self.session.date} {self.session.time} {self.session.room} {self.subject.name} {self.group_id} {self.nos}'

if __name__ == '__main__':
    file1 = open("MONTHI.in", 'r')
    file2 = open("CATHI.in", 'r')
    file3 = open("LICHTHI.in", 'r')

    subject = {}
    n = int(file1.readline().rstrip())
    for _ in range(n):
        tmp = Subject(file1.readline().strip(), file1.readline().strip(), file1.readline().strip())
        subject[tmp.id] = tmp

    session = {}
    m = int(file2.readline().rstrip())
    for i in range(m):
        tmp = Session(i + 1, file2.readline().strip(), file2.readline().strip(), file2.readline().strip())
        session[tmp.id] = tmp

    l = []
    k = int(file3.readline().rstrip())
    for i in range(k):
        tmp = file3.readline().rstrip().split()
        l.append(Schedule(session[tmp[0]], subject[tmp[1]], tmp[2], tmp[3]))
    for x in sorted(l, key=lambda x : (datetime.strptime(x.session.date + " " + x.session.time, "%d/%m/%Y %H:%M"), x.session.id)):
        print(x)