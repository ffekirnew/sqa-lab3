from src.activity_1.max_of_three_numbers import max_of_three_numbers


def test_path_1_a_is_max():
    assert max_of_three_numbers(5, 2, 3) == 5
    assert max_of_three_numbers(10, 10, 5) == 10  # Edge case: a == b
    assert max_of_three_numbers(7, 5, 7) == 7  # Edge case: a == c


def test_path_2_c_is_max_after_a_ge_b():
    assert max_of_three_numbers(3, 2, 5) == 5
    assert max_of_three_numbers(5, 5, 10) == 10  # Edge case: a == b


def test_path_3_b_is_max():
    assert max_of_three_numbers(2, 5, 3) == 5
    assert max_of_three_numbers(1, 5, 5) == 5  # Edge case: b == c


def test_path_4_c_is_max_after_a_lt_b_and_b_lt_c():
    assert max_of_three_numbers(2, 3, 5) == 5
    # Edge case: b == c, but still path 4
    assert max_of_three_numbers(1, 2, 2) == 2


def test_negative_numbers():
    assert max_of_three_numbers(-1, -5, -3) == -1  # Path 1
    assert max_of_three_numbers(-3, -5, -1) == -1  # Path 2
    assert max_of_three_numbers(-5, -1, -3) == -1  # Path 3
    assert max_of_three_numbers(-5, -3, -1) == -1  # Path 4


def test_mixed_numbers():
    assert max_of_three_numbers(0, -5, 10) == 10
    assert max_of_three_numbers(-10, 0, -5) == 0
    assert max_of_three_numbers(5, -2, 0) == 5
    assert max_of_three_numbers(0, 0, 0) == 0
