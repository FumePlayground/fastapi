import pytest
from utils import some_utility_function  # assuming utility functions are defined in utils.py

def test_some_utility_function():
    # Test case 1
    result = some_utility_function("test_input_1")
    expected_value = "expected_output_1"
    assert result == expected_value, f"Expected {expected_value} but got {result}"

    # Test case 2
    result = some_utility_function("test_input_2")
    expected_value = "expected_output_2"
    assert result == expected_value, f"Expected {expected_value} but got {result}"

    # Add more test cases as needed
