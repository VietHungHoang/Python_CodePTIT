class Team:
    def __init__(self, id, name, school):
        self.id = 'Team{:02d}'.format(id)
        self.name = name
        self.school = school
class Student:
    def __init__(self, id, name, team):
        self.id = 'C{:03d}'.format(id)
        self.name = name
        self.team = team
    def __str__(self):
        return f'{self.id} {self.name} {self.team.name} {self.team.school}'
if __name__ == '__main__':
    teams = {}
    for i in range(int(input())):
        tmp = Team(i + 1, input(), input())
        teams[tmp.id] = tmp
    students = []
    for i in range(int(input())):
        students.append(Student(i + 1, input(), teams[input()]))
    students.sort(key = lambda x : x.name)
    print(*students, sep = '\n')