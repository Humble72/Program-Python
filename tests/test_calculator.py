import pytest
from logic.calculator import calculate_fuel_cost


def test_calculate_fuel_cost_valid():
    assert calculate_fuel_cost(50.0, 6.50) == 325.0


def test_calculate_fuel_cost_zero():
    assert calculate_fuel_cost(0.0, 6.50) == 0.0


def test_calculate_fuel_cost_negative_values():
    with pytest.raises(ValueError, match="nie mogą być ujemne"):
        calculate_fuel_cost(-10.0, 6.50)
