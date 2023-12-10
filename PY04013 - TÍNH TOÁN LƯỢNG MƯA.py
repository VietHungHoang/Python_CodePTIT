from datetime import *
    
class Station:
    next_id = 1
    def __init__(self, name, start, end, rainfall):
        self.name = name
        self.id = f"T{Station.next_id:02d}"
        Station.next_id += 1
        self.rainfall = 0
        self.total_time = 0
        
        self.update(start, end, rainfall)

        

    def update(self, start, end, rainfall):
        time_format = "%H:%M"
        time_start = datetime.strptime(start, time_format)
        time_end = datetime.strptime(end, time_format)
        self.total_time += (time_end - time_start).total_seconds()
        self.rainfall += rainfall
        
    def __str__(self):
        return self.id + " " + self.name + " " + (f"%.2f" % (self.rainfall * 3600 / self.total_time))

if __name__ == '__main__':
    d = {}
    for _ in range(int(input())):
        name = input()
        if name in d: d[name].update(input(), input(), int(input()))
        else: d[name] = Station(name, input(), input(), int(input()))
    for x in d: print(d[x])