from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float):
    """Проверяет введеное значение."""
    if your_number <= 0:
        return
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {calculatesquareroot(your_number)}')


print(message)
calc(25.5)
