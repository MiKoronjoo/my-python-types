import math


class Complex(object):
    def __init__(self: 'Complex', real: [int, float], imag: [int, float]) -> None:
        self._real = real / 1
        self._imag = imag / 1

    @property
    def real(self):
        return self._real

    @property
    def imag(self):
        return self._imag

    def __add__(self: 'Complex', other: 'Complex') -> 'Complex':
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self: 'Complex', other: 'Complex') -> 'Complex':
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self: 'Complex', other: 'Complex') -> 'Complex':
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def conjugate(self: 'Complex') -> 'Complex':
        return Complex(self.real, -self.imag)

    def __truediv__(self: 'Complex', other: 'Complex') -> 'Complex':
        denominator = (other * other.conjugate()).real
        numerator = self * other.conjugate()
        return Complex(numerator.real / denominator,
                       numerator.imag / denominator)

    def __str__(self: 'Complex') -> str:
        part1 = ''
        part2 = ''
        if self.real != 0:
            part1 = str(self.real)
        if self.imag != 0:
            if self.imag > 0:
                part2 = '+' + str(self.imag) + 'i'
            else:
                part2 = str(self.imag) + 'i'
        return part1 + part2

    @property
    def magnitude(self) -> float:
        return round((self.real ** 2 + self.imag ** 2) ** 0.5, 2)

    @property
    def cart_to_polar(self):
        theta = round(math.atan(self.real / self.imag), 2)
        return [self.magnitude, theta]

    @property
    def polar_to_cart(self) -> 'Complex':
        x = round(self.real * math.cos(self.imag), 2)
        y = round(self.real * math.sin(self.imag), 2)
        return Complex(x, y)

    def __pow__(self, power: float) -> 'Complex':
        return Complex(self.real ** power, self.imag ** power)

    @staticmethod
    def determinant(a: int, b: int, c: int, d: int) -> int:
        return a * d - b * c

    @staticmethod
    def root(a, r, s) -> list:
        delta = r ** 2 - 4 * s * a  # r^2 - 4sa

        if delta < 0:
            n = (-delta) ** 0.5
            x1 = -r / 2 * a
            x2 = n / 2 * a
            x3 = -1
            return [x1, x2, x3]
        elif delta == 0:
            x1 = -r / (2 * a)
            x2 = 0
            return [x1, x2]
        else:
            n = delta ** 0.5
            x1 = (-r + n) / (2 * a)
            x2 = (-r - n) / (2 * a)
            x3 = 1
            return [x1, x2, x3]

    @staticmethod
    def bairstow(n, a) -> list:
        roots = []
        r = -1
        s = 1

        def rec_bairstow(n, a, b, c, r, s) -> list:
            b += [a[0]]
            b += [a[1] + r * b[0]]
            for i in range(2, len(a)):
                b += [a[i] + r * b[i - 1] + s * b[i - 2]]
            c += [b[0]]
            c += [b[1] + r * c[0]]
            for i in range(2, len(a) - 1):
                c += [b[i] + r * c[i - 1] + s * c[i - 2]]
            d = Complex.determinant(c[-1], c[-2], c[-2], c[-3])
            if d == 0:
                return rec_bairstow(n, a, b, c, r + 0.1, s - 0.1)
            d1 = Complex.determinant(-b[-1], c[-2], -b[-2], c[-3])
            d2 = Complex.determinant(c[-1], -b[-1], c[-2], -b[-2])
            new_r = r + (d1 / d)
            new_s = s + (d2 / d)
            return [new_r, new_s]

        if len(a) > 3:
            b = []
            c = []
            coef = rec_bairstow(n, a, b, c, r, s)
            e = 0.000001

            while abs(r - coef[0]) > e or abs(s - coef[1]) > e:
                r = coef[0]
                s = coef[1]
                b = []
                c = []
                coef = rec_bairstow(n, a, b, c, r, s)
            roots += [Complex.root(1, -r, -s)]
            return roots + Complex.bairstow(n - 2, b[:-2])

        if len(a) == 3:
            return [Complex.root(a[0], a[1], a[2])]
        if len(a) == 2:
            return [[-a[1] / (a[0]), 0, 0]]
        return [[0, 0, 0]]


if __name__ == '__main__':
    a = Complex(4, -5)
    b = Complex(-8, 9)
    print('num1:\t\t', a)
    print('num2:\t\t', b)
    print('num1 conj:\t', a.conjugate())
    print('num2 conj:\t', b.conjugate())
    print('add:\t\t', a + b)
    print('sub:\t\t', a - b)
    print('mul:\t\t', a * b)
    print('div:\t\t', a / b)
