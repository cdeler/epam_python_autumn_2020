import pytest
from calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(65536, True), (12, False), (8, True), (512, True), (777, False), (13, False)],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
