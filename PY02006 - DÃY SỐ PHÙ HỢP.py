def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = sorted(list(map(int, input().split())))
        b = sorted(list(map(int, input().split())))
        print(check(a, b))
