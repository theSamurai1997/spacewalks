import pytest
from eva_data_analysis import text_to_duration, calculate_crew_size

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected value for durations
    with a non-zero minute component
    """
    assert text_to_duration("10:20") == pytest.approx(10.33333333)


def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected value for durations
    with typical whole hour durations
    """
    assert text_to_duration("10:00") == 10


@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result


# Edge cases
def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected ground truth values
    for edge case where crew is an empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None