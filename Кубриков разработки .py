from calculator import Calculator
from complex_number import ComplexNumber


def get_complex_number():
    """Ввод комплексного числа с консоли."""
    while True:
        try:
            real = float(input("Введите действительную часть: "))
            imag = float(input("Введите мнимую часть: "))
            return ComplexNumber(real, imag)
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")


def main():
    """Основная функция программы."""
    calculator = Calculator()

    while True:
        print("\nВыберите операцию:")
        print("1 - Сложение")
        print("2 - Умножение")
        print("3 - Деление")
        print("4 - Выход")

        choice = input("Введите номер операции: ")

        if choice == "1":
            num1 = get_complex_number()
            num2 = get_complex_number()
            result = calculator.add(num1, num2)
            print(f"Результат: {result}")
        elif choice == "2":
            num1 = get_complex_number()
            num2 = get_complex_number()
            result = calculator.multiply(num1, num2)
            print(f"Результат: {result}")
        elif choice == "3":
            num1 = get_complex_number()
            num2 = get_complex_number()
            try:
                result = calculator.divide(num1, num2)
                print(f"Результат: {result}")
            except ZeroDivisionError:
                print("Деление на ноль невозможно.")
        elif choice == "4":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if _name_ == "_main_":
    main()