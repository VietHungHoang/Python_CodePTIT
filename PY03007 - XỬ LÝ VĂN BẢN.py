import re
if __name__ == '__main__':
    s = ""
    while True:
        try: s += input()
        except: break

    pattern = r"[\s\w:,]+"
    s = re.findall(pattern, s)
    for i in s:
        x = i.lower().split()
        x[0] = x[0].title()
        print(*x)