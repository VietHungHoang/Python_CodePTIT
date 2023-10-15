fibo = [1] * 93

for i in range(3, 93):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

if __name__ == '__main__':
    for t in range(int(input())):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            print(fibo[i], end=' ')
        print()
