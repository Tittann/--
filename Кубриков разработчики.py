class ComplexNumber:
    """Представляет комплексное число."""

    def __init__(self, real, imag):
        """Инициализирует комплексное число."""
        self.real = real
        self.imag = imag

    def __str__(self):
        """Возвращает строковое представление комплексного числа."""
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    def __add__(self, other):
        """Определяет операцию сложения."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("Операнд должен быть комплексным числом.")

    def __mul__(self, other):
        """Определяет операцию умножения."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real * other.real - self.imag * other.imag,
                self.real * other.imag + self.imag * other.real,
            )
        else:
            raise TypeError("Операнд должен быть комплексным числом.")

    def __truediv__(self, other):
        """Определяет операцию деления."""
        if isinstance(other, ComplexNumber):
            denominator = other.real**2 + other.imag**2
            return ComplexNumber(
                (self.real * other.real + self.imag * other.imag) / denominator,
                (self.imag * other.real - self.real * other.imag) / denominator,
            )
        else:
            raise TypeError("Операнд должен быть комплексным числом.")