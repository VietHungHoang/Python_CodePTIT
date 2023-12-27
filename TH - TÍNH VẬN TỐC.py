from datetime import *

class Player:
    def __init__(self, name, city, end):
        self.id = ""
        for i in city.split():
            self.id += i[0].upper()
        for i in name.split():
            self.id += i[0].upper()
        self.city = city
        self.name = name

        time_format = "%H:%M"
        time_in = datetime.strptime("06:00", time_format)
        time_end = datetime.strptime(end, time_format)
        self.total_time = int((time_end - time_in).total_seconds() // 60)
        self.velocity = round((60 * 120) / self.total_time)

    def __str__(self):
        return self.id + " " + self.name + " " + self.city + " " + str(self.velocity) + " Km/h"
        
if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        l.append(Player(input(), input(), input()))
    l.sort(key = lambda x: x.total_time)
    print(*l, sep = '\n')