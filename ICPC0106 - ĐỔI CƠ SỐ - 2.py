if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        bin_number = input()
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
