def check(s):
    try:
        s = list(map(int, s.split(".")))
        for x in s:
            if x < 0 or x > 255: return False
        return len(s) == 4
    except: return False



if __name__ == "__main__":
    for _ in range(int(input())):
        if check(input()): print("YES")
        else: print("NO")