"""
Методы работы с данными
"""
import numpy as np


def to_polynom(x, order=2):
    """
    Преобразование к полиному
    :param x: исходные данные
    :param order: степень полинома
    """
    order_range = range(2, order + 1, 1)
    out = np.copy(x)
    for i in order_range:
        out = np.hstack([out, np.power(x, i)])
    return out
