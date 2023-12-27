priority = [1.5, 1, 0]
class Candidate:
    def __init__(self, id, name, mark, ethnicity, area):
        self.id = 'TS{0:0>2}'.format(id)
        self.name = ''.join([x.title() + " " for x in name.split()]).strip()
        self.mark = float(mark)
        self.mark += 0 if ethnicity == 'Kinh' else 1.5
        self.mark += priority[int(area) - 1]

    def __str__(self):
        return f'{self.id} {self.name} ' + '%.1f' % self.mark + (" Do" if self.mark >= 20.5 else " Truot")

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        l.append(Candidate(i + 1, input().strip(), input().strip(), input().strip(), input().strip()))
    for x in sorted(l, key = lambda x : (-x.mark, x.id)): print(x)