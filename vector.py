# coding: utf-8

from math import hypot


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector(x, y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __repr__(self):
        return 'Vector(x: %s, y: %s)' % (self.x, self.y)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print v1 + v2
    print v1 * v2
    print abs(v1 * v2)
    print bool(Vector(0, 0))
