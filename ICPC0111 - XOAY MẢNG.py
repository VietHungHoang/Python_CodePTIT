if __name__ == '__main__':
    for _ in range(int(input())):
        n, idx = map(int, input().split())
        list = input().split()
        print(*(list[idx:] + list[:idx]))
