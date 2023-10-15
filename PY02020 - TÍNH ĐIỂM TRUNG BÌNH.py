if __name__ == '__main__':

    n = int(input())
    a = list(map(float, input().split()))
    ma, mi = max(a), min(a)
    lst = []
    for i in a:
        if i != ma and i != mi:
            lst.append(i)
    print("{:.2f}".format(sum(lst) / len(lst)))
