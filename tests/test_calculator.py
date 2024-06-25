import pytest

from contextlib import nullcontext as does_not_raise

from src.calculator import Calculator


class TestCalculator:
    @pytest.mark.parametrize(
        "a, b, res, expectation",
        [
            (25, 5, 5, does_not_raise()),
            (1, 2, 0.5, does_not_raise()),
            (6, 0, -6, pytest.raises(ZeroDivisionError)),
        ],
    )
    def test_divide(self, a, b, res, expectation):
        with expectation:
            assert Calculator().divide(a, b) == res

    @pytest.mark.parametrize(
        "a, b, res, expectation",
        [
            (5, 5, 25, does_not_raise()),
            (1, "", 2, pytest.raises(TypeError)),
            (6, -2, -12, does_not_raise()),
        ],
    )
    def test_multiply(self, a, b, res, expectation):
        with expectation:
            assert Calculator().multiply(a, b) == res

    @pytest.mark.parametrize(
        "a, b, res, expectation",
        [
            (5, 5, 10, does_not_raise()),
            (11, -22, -11, does_not_raise()),
            (6, "", 4, pytest.raises(TypeError)),
        ],
    )
    def test_add(self, a, b, res, expectation):

        with expectation:
            assert Calculator().add(a, b) == res

    @pytest.mark.parametrize(
        "a, b, res, expectation",
        [
            (5, 2, 3, does_not_raise()),
            (1, 4, -3, does_not_raise()),
            (16, -2, 18, does_not_raise()),
        ],
    )
    def test_subtract(self, a, b, res, expectation):
        with expectation:
            assert Calculator().subtract(a, b) == res
