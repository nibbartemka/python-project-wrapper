import math

import pytest

from src.geometric_lib import Circle


class TestCircleArea:
    """Circle.area property."""

    @pytest.mark.parametrize(
        ("radius", "expected"),
        [
            (1, math.pi),
            (2, 4 * math.pi),
            (0.5, 0.25 * math.pi),
            (10, 100 * math.pi),
            (2.5, 6.25 * math.pi),
        ],
    )
    def test_area(self, radius: float, expected: float) -> None:
        """Area equals pi * r**2 for various inputs."""
        assert Circle(radius).area == pytest.approx(expected)

    @pytest.mark.parametrize("radius", [0, -1, -0.5, -100])
    def test_area_non_positive_raises(self, radius: float) -> None:
        """Non-positive radius raises ValueError."""
        with pytest.raises(ValueError, match="more than 0"):
            Circle(radius).area


class TestCirclePerimeter:
    """Circle.perimeter property."""

    @pytest.mark.parametrize(
        ("radius", "expected"),
        [
            (1, 2 * math.pi),
            (2, 4 * math.pi),
            (0.5, math.pi),
            (10, 20 * math.pi),
            (2.5, 5 * math.pi),
        ],
    )
    def test_perimeter(self, radius: float, expected: float) -> None:
        """Perimeter equals 2 * pi * r for various inputs."""
        assert Circle(radius).perimeter == pytest.approx(expected)

    @pytest.mark.parametrize("radius", [0, -1, -0.5, -100])
    def test_perimeter_non_positive_raises(self, radius: float) -> None:
        """Non-positive radius raises ValueError."""
        with pytest.raises(ValueError, match="more than 0"):
            Circle(radius).perimeter
