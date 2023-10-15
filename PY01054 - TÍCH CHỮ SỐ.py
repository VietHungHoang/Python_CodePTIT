if __name__ == '__main__':
    for t in range(int(input())):
        res = 1
        for x in input():
            if x != '0': res *= int(x)
        print(res)