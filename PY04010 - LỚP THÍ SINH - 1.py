class Student:
    def __init__(self, name, dob, mark1, mark2, mark3):
        self.name = name
        self.dob = dob
        self.marks = mark1 + mark2 + mark3
    
    def __str__(self):
        return self.name + " " + self.dob + " " + ("%.1f" % self.marks)


if __name__ == '__main__':
    print(Student(input(), input(), float(input()), float(input()), float(input())))