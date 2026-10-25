from abc import ABC, abstractmethod

type Numeric = int | float


class Shape(ABC):
    @property
    @abstractmethod
    def perimeter(self) -> Numeric:
        pass

    @property
    @abstractmethod
    def area(self) -> Numeric:
        pass
