priority = {'1' : 2.0, '2': 1.5, '3' : 1.0, '4' : 0}
subject = {'A' : "TOAN", 'B' : "LY", 'C' : "HOA"}

class Candidate:
    def __init__(self, id, name, code, mark1, mark2):
        self.id = 'GV{0:0>2}'.format(id)
        self.name = name
        self.subject = subject[code[0]]
        self.mark = mark1 * 2 + mark2
        self.mark += priority[code[1]]
    def __str__(self):
        return f'{self.id} {self.name} {self.subject}' + " {:.1f} ".format(self.mark) + ("TRUNG TUYEN" if self.mark >= 18.0 else "LOAI")

if __name__ == '__main__':
    a = []
    for i in range(int(input())):
        a.append(Candidate(i + 1, input(), input(), float(input()), float(input())))
    a.sort(key = lambda x : -x.mark)
    for x in a: print(x)

