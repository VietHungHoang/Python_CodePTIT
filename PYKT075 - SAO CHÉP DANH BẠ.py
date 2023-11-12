class Contact:
    def __init__(self, date, full_name, phone_number):
        d = date.split()
        self.date = d[1]
        self.full_name = full_name
        l = full_name.split()
        self.name = l[-1]
        self.sur_middle_name = ""
        for i in range(len(l) - 1):
            self.sur_middle_name += l[i] + " "
        self.phone_number = phone_number
    def toString(self):
        return self.full_name + ": " + self.phone_number + " " + self.date + "\n"

def repair_string(s):
    s = s.replace("\n", "")
    return s

if __name__ == "__main__":
    l = []
    with open("SOTAY.txt", "r") as note:
        with open("DIENTHOAI.txt", "w") as contact:
            d = [repair_string(x) for x in note.readlines()]
            idx = 0
            while idx < len(d):
                if "/" in d[idx]:
                    date = d[idx]
                    idx += 1
                else:
                    l.append(Contact(date, d[idx], d[idx+1]))
                    idx += 2
            l.sort(key = lambda x: (x.name, x.sur_middle_name))
            for x in l: contact.write(x.toString())