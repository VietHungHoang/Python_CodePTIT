if __name__ == '__main__':
    file = open("CONTACT.in", 'r')
    res = []
    for line in file:
        for x in line.split():
            try:
                if int(x) > 2 * 10**9: res.append(x)
            except:
                res.append(x)
    print(*sorted(res))
