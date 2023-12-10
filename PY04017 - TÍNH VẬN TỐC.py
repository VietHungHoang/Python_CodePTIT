# So sánh vận tốc ở dạnh float, chỉ làm tròn khi in
class CuaRo:
    def __init__(self, name, city, endTime):
        self.id = ''.join([x[0] for x in city.split()]) + ''.join([x[0] for x in name.split()])
        self.name = name
        self.city = city
        h, m = map(int, endTime.split(':'))
        self.velocity = (120 / (h - 6 + m / 60))

    def __str__(self):
        return f'{self.id} {self.name} {self.city} {round(self.velocity)} Km/h'
if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        a.append(CuaRo(input(), input(), input()))
    a.sort(key = lambda x : -x.velocity)
    for x in a: print(x)