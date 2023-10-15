def check(s):
    for i in range(2, len(s), 2):
        if s[i] != s[0]: return False
    return len(s) % 2 != 0 and s[0] != s[1]

if __name__ == '__main__':
    for t in range(int(input())):
        print("YES" if check(input()) else "NO")
