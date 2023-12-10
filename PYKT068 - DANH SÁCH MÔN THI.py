class Exam:
    def __init__(self, id, name, format):
        self.id = id
        self.name = name
        self.format = format
    
    def __str__(self):
        return f'{self.id} {self.name} {self.format}'

if __name__ == '__main__':
    n = int(input())
    exams = []
    for _ in range(n):
        exams.append(Exam(input(), input(), input()))
    for x in sorted(exams, key = lambda x : x.id):
        print(x)