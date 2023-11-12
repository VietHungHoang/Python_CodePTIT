class Student:
    def __init__(self, id, name, total):
        self.id = f"{id:02d}"
        self.name = name
        self.avg = round(total / 12 + 0.01, 1)
    def getPerfomance(self):
        if self.avg >= 9: return "XUAT SAC"
        elif self.avg >= 8: return "GIOI"
        elif self.avg >= 7: return "KHA"
        elif self.avg >= 5: return "TB"
        else: return "YEU"
    def __str__(self):
        return self.id + " " + self.name + " " + f"%.1f" % self.avg + " " + self.getPerfomance() 
if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        name = input()
        mark = list(map(float, input().split()))
        l.append(Student(i + 1, name, sum(mark) + mark[0] + mark[1]))
    l.sort(key = lambda x : (-x.avg, x.id))
    for x in l: print(x)

            