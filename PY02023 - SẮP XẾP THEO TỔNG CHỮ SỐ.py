if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        a = input().split()
        a.sort(key=lambda s: (sum(int(i) for i in s), int(s)))
        print(*a)
