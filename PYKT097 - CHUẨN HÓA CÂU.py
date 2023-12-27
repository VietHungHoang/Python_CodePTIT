if __name__ == '__main__':
    while True:
        try:
            s = input().capitalize().strip()
            sign = ""
            for x in ('.', '?', '!'):
                if s.endswith(x): sign = x
            if sign == "": sign = '.'
            else: s = s[0:len(s) - 1]
            print("".join([x + " " for x in s.split()]).strip() + sign)
        except: break