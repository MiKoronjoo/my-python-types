class Complex(object):
    def __init__(self: 'Complex', real: [int, float], imag: [int, float]) -> None:
        self._real = real
        self._imag = imag

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
