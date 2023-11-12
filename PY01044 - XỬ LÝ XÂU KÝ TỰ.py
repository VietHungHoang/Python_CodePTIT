if __name__ == "__main__": 
    a = [i.lower() for i in input().split()]
    b = [i.lower() for i in input().split()]
    d1, d2, d3 = {}, {}, {}
    for i in a:
        d1[i] = 1
        d2[i] = 1
    for i in b:
        d1[i] = 1
        d3[i] = 1
        
    for i in sorted(d1):
        print(i, end = ' ')
    print()

    for i in sorted(d2):
        if i in d3:
            print(i, end = ' ')