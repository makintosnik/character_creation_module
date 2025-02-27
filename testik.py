from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float):
    """Проверяет введеное значение."""
    if your_number <= 0:
        return
    result: float = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого '
          f'вами числа. Это будет: {result}')


print(message)
calc(25.5)
