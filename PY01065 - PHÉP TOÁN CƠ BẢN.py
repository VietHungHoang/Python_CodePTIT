def gene(s):
    if s[0] == '?' and s[1] == '?':
        return [i for i in range(10, 100)]
    elif s[0] == '?':
        return [i * 10 + int(s[1]) for i in range(1, 10)]
    elif s[1] == '?': return [10 * int(s[0]) + i for i in range(0, 10)]
    else: return [int(s)]

def solve(s):
    if not(s[3] == '/' or s[3] == '*'):
        a = gene(s[:2])
        b = gene(s[5:7])
        c = gene(s[-2:])
        for x in a:
            for y in b:
                if s[3] == '+' or s[3] == '?':
                    if x + y in c:
                        print(x, '+', y, '=', x + y)
                        return
                if s[3] == '-' or s[3] == '?':
                    if x - y in c:
                        print(x, '-', y, '=', x - y)
                        return
    print("WRONG PROBLEM!")
    return   

if __name__ == "__main__": 
    for _ in range(int(input())):
        solve(input())


