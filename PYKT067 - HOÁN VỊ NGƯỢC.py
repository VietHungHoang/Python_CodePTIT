from itertools import permutations

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [i + 1 for i in range(n)]
        res = list(permutations(a))[::-1]
        print(len(res))
        for x in res:
            print(*x, sep = '', end = ' ')
        print()


