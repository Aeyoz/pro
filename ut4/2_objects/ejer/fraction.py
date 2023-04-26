class Fraction:
    def gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a

    def __init__(self, num: int, den: float):
        div = Fraction.gcd(num, den)
        self.num = num / div
        self.den = den / div

    def __str__(self):
        length = max(len(f"{self.num:.0f}"), len(f"{self.den:.0f}"))
        return f"{self.num:.0f}\n{'—'*length}\n{self.den:.0f}"

    def __add__(self, other):
        num = self.num*other.den+other.num*self.den
        den = self.den*other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num*other.den-other.num*self.den
        den = self.den*other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num*other.num
        den = self.den*other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num*other.den
        den = self.den*other.num
        return Fraction(num, den)

first_fraction = Fraction(25,30)
second_fraction = Fraction(40,45)
result = first_fraction + second_fraction
print(result)
result = first_fraction - second_fraction
print(result)
result = first_fraction * second_fraction
print(result)
result = first_fraction / second_fraction
print(result)