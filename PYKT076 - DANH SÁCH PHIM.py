from  datetime import datetime
t = {}
class Film:
    def __init__(self, id, type, start, name, episode):
        self.id = 'P{0:0>3}'.format(id)
        self.type = t[type]
        self.start = start
        self.episode = episode
        self.name = name

    def __str__(self):
        return f'{self.id} {self.type} {self.start} {self.name} {self.episode}'

if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        t['TL{0:0>3}'.format(i + 1)] = input()
    l = []
    for i in range(m):
        l.append(Film(i + 1, input(), input(), input(), int(input())))
    for x in sorted(l, key = lambda x : (datetime.strptime(x.start, "%d/%m/%Y"), x.name, -x.episode)):
        print(x)