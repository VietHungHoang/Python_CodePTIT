if __name__ == '__main__':
    with open ("CONTACT.in", "r") as inp:
            n = inp.readline()
            for _ in range(int(n)):
                n = int(inp.readline())
                bin_number = inp.readline()
                dec_number = int(bin_number, 2)
                if n == 2: print(bin_number)
                elif n == 8: print(oct(dec_number)[2::])
                elif n == 16: print(hex(dec_number)[2::].upper())
                else: 
                    digit = ""
                    while dec_number:
                        tmp = dec_number % 4
                        digit = str(tmp) + digit
                        dec_number //= 4
                    print(digit)