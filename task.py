from math import sqrt
from typing import Optional


def add_numbers(x_number: int, y_number: int) -> int:
    return x_number + y_number


def calculate_square_root(number: int) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return
    root: float = calculate_square_root(your_number)
    return ('Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {root}')


x_number: int = 10
y_number: int = 5

print('Сумма чисел: ', add_numbers(x_number, y_number))
print(calc(25.5))
