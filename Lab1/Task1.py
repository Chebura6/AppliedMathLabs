import math
import numpy as np

def right(f, x, h):
    return (f(x + h) - f(x)) / h


def left(f, x, h):
    return (f(x) - f(x - h)) / h


def central(f, x, h, a):
    i = x / h
    x_l = a + h * (i - 1)
    y_l = f(x_l)
    x_r = a + h * (i + 1)
    y_r = f(x_r)
    return (y_r - y_l) / (2 * h)
