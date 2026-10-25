import pytest
from src.geometric_lib import Rectangle


class TestRectangleArea:
    """Rectangle.area property."""

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (1, 1, 1),
            (2, 3, 6),
            (10, 5, 50),
            (2.5, 4.0, 10.0),
            (1.5, 1.5, 2.25),
        ],
    )
    def test_area(self, a: float, b: float, expected: float) -> None:
        """Area equals a * b for various inputs."""
        assert Rectangle(a, b).area == pytest.approx(expected)

    @pytest.mark.parametrize(("a", "b"), [(-1, -1), (-0.5, -100), (0, 0)])
    def test_area_non_positive_raises(self, a: float, b: float) -> None:
        """Non-positive a, b raises ValueError."""
        with pytest.raises(ValueError, match="more than 0"):
            Rectangle(a, b).area


class TestRectanglePerimeter:
    """Rectangle.perimeter property."""

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (1, 1, 4),
            (2, 3, 10),
            (10, 5, 30),
            (2.5, 4.0, 13.0),
            (1.5, 1.5, 6.0),
        ],
    )
    def test_perimeter(self, a: float, b: float, expected: float) -> None:
        """Perimeter equals 2*a + 2*b."""
        assert Rectangle(a, b).perimeter == pytest.approx(expected)

    @pytest.mark.parametrize(("a", "b"), [(-1, -1), (-0.5, -100), (0, 0)])
    def test_perimeter_non_positive_raises(self, a: float, b: float) -> None:
        """Non-positive a, b raises ValueError."""
        with pytest.raises(ValueError, match="more than 0"):
            Rectangle(a, b).perimeter
