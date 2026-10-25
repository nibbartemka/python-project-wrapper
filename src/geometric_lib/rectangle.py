from .base import Numeric, Shape


class Rectangle(Shape):
    def __init__(self, a: Numeric, b: Numeric) -> None:
        if a <= 0 or b <= 0:
            raise ValueError("sides of rectangle have to be more than 0")

        self.a = a
        self.b = b

    @property
    def perimeter(self) -> Numeric:
        return 2 * self.a + 2 * self.b

    @property
    def area(self) -> Numeric:
        return self.a * self.b
