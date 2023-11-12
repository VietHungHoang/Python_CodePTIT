class Student:
    def __init__(self, name, submit, mark):
        self.name = name
        self.submit = submit
        self.mark = mark
    
    def __str__(self):
        return self.name + " " + str(self.submit) + " " + str(self.mark)

if __name__ == '__main__':
    n = int(input())
    l = [0] * n
    for i in range(n):
        name = input()
        submit, mark = map(int, input().split())
        l[i] = Student(name, submit, mark)
    l.sort(key = lambda x : (-x.submit, x.mark, x.name))
    for x in l: print(x)
