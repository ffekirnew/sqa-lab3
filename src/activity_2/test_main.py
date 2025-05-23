import pytest

from src.activity_2.main import check_number


@pytest.mark.parametrize(
    "num, expected_output",
    [
        (2, "Positive even number"),  # Positive even
        (3, "Positive odd number"),  # Positive odd
        (-1, "Negative number"),  # Negative
        (0, "Zero"),  # Zero
    ],
)
def test_check_number(num, expected_output, capsys):
    check_number(num)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
