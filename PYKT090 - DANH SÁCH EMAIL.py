if __name__ == '__main__':
    file = open('CONTACT.in', 'r')
    res = set()
    for line in file:
        res.add(line.lower().strip())
    for x in sorted(res): print(x)