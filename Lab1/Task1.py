import math
import numpy as np

a = 0
b = 10
h = 0.1

n = round((b - a) / h)


def right(f, x):
    global h
    return (f(x + h) - f(x)) / h


def left(f, x):
    global h
    return (f(x) - f(x - h)) / h


def central(f, x):
    global a
    global h
    i = x / h
    x_l = a + h * (i - 1)
    y_l = f(x_l)
    x_r = a + h * (i + 1)
    y_r = f(x_r)
    return (y_r - y_l) / (2 * h)

#
# x0 = 5.625
# print(right(f1, x0))
# print(left(f1, x0))
# print(central(f1, x0))