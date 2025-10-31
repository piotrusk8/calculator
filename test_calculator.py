import pytest
from calculator import Calculator


@pytest.mark.parametrize(
    "op1, op2, expected",
    [
        (1, 2, 3.0),
        (1.5, 2.5, 4.0),
        (-1, 1, 0.0),
        (1e6, 1e6, 2e6),
    ],
)
def test_sum(op1, op2, expected):
    assert Calculator(op1, op2).sum() == pytest.approx(expected)


@pytest.mark.parametrize(
    "op1, op2, expected",
    [
        (5, 2, 3.0),
        (2.5, 5.5, -3.0),
        (-3, -3, 0.0),
        (1e6, 1, 999999.0),
    ],
)
def test_sub(op1, op2, expected):
    assert Calculator(op1, op2).sub() == pytest.approx(expected)


@pytest.mark.parametrize(
    "op1, op2, expected",
    [
        (3, 4, 12.0),
        (2.5, 2, 5.0),
        (-3, 2, -6.0),
        (0, 999, 0.0),
    ],
)
def test_mul(op1, op2, expected):
    assert Calculator(op1, op2).mul() == pytest.approx(expected)


@pytest.mark.parametrize(
    "op1, op2, expected",
    [
        (6, 3, 2.0),
        (7.5, 2.5, 3.0),
        (-9, 3, -3.0),
        (1, 4, 0.25),
    ],
)
def test_div(op1, op2, expected):
    result = Calculator(op1, op2).div()
    assert result == pytest.approx(expected)
    assert isinstance(result, float)


def test_div_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        Calculator(1, 0).div()