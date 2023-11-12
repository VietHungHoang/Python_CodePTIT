from math import gcd
class Fraction:

    def __init__(self, numerator = None, denominator = None):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        c = Fraction()
        c.denominator = self.denominator * other.denominator
        c.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        c.reduce()
        return c

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def reduce(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

if __name__ == '__main__':
    list = list(map(int, input().split()))
    a = Fraction(list[0], list[1])
    b = Fraction(list[2], list[3])
    print(a + b)
