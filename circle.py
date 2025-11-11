# Файл: circle.py
# Содержит функции для вычисления площади и длины окружности (периметра) круга.

import math


def area(r):
    """
    Вычисляет площадь круга.

    Аргументы:
        r (float): радиус круга

    Возвращает:
        float: площадь круга

    Исключения:
        TypeError: если радиус не является числом
        ValueError: если радиус отрицательный

    Пример:
        area(3) -> 28.27
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    
    if r < 0:
        raise ValueError("Радиус должен быть положительным числом")
    
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности (периметр круга).

    Аргументы:
        r (float): радиус круга

    Возвращает:
        float: длину окружности

    Исключения:
        TypeError: если радиус не является числом
        ValueError: если радиус отрицательный

    Пример:
        perimeter(3) -> 18.85
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    
    if r < 0:
        raise ValueError("Радиус должен быть положительным числом")
    
    return 2 * math.pi * r
    
    