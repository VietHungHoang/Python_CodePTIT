from math import gcd
class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def reduce(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

if __name__ == '__main__':
    list = list(map(int, input().split()))
    a = Fraction(list[0], list[1])
    a.reduce()
    print(a)
