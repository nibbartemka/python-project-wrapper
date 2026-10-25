from math import pi

from .base import Numeric, Shape


class Circle(Shape):
    def __init__(self, radius: Numeric) -> None:
        if radius <= 0:
            raise ValueError("radius has to be more than 0")

        self.radius = radius

    @property
    def perimeter(self) -> Numeric:
        return 2 * pi * self.radius

    @property
    def area(self) -> Numeric:
        return pi * self.radius**2
