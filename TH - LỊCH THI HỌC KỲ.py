from datetime import datetime
if __name__ == '__main__':

    n, m = map(int, input().split())

    d = {}

    for i in range(n):
        s = input()
        d[s] = input()

    class LichThi:
        def __init__(self, maMon, ngayThi, gioThi, nhomThi, monThi, cnt):
            self.ID = 'T{:03d}'.format(cnt)
            self.maMon = maMon
            self.ngayThi = ngayThi
            self.gioThi = gioThi
            self.nhomThi = nhomThi
            self.monThi = monThi
            Day, Month, Year = map(int, ngayThi.split('/'))
            Hour, Minute = map(int, gioThi.split(':'))
            self.ngayThiGioThi = datetime(Year, Month, Day, Hour, Minute)

    a = []

    for i in range(m):
        s = input().split()
        a.append(LichThi(s[0], s[1], s[2], s[3], d[s[0]], i + 1))

    a.sort(key = lambda i : (i.ngayThiGioThi, i.ID))

    for i in a:
        print(i.ID, i.maMon, i.monThi, i.ngayThi, i.gioThi, i.nhomThi)