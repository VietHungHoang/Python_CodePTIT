t = int(input())
for _ in range(t):
    s = input()
    if s[0:2] == s[len(s) - 2: : 1]: print("YES")
    else: print("NO")