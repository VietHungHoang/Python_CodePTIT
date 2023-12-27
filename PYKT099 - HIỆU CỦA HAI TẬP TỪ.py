if __name__ == '__main__':
    file = open("DATA1.in", 'r')
    a = set()
    for line in file:
        a.update(line.lower().strip().split())
    file.close()
    file = open("DATA2.in", 'r')
    b = set()
    for line in file:
        b.update(line.lower().strip().split())
    file.close()
    print(*sorted(a.difference(b)))
    print(*sorted(b.difference(a)))