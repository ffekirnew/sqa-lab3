from src.activity_3.annotated_code import calculate_grade


def test_default_grade():
    assert calculate_grade(50, False) == "F"


def test_absent_grade():
    assert calculate_grade(100, True) == "I"


def test_grade_A():
    assert calculate_grade(95, False) == "A"


def test_grade_B():
    assert calculate_grade(85, False) == "B"


def test_grade_C():
    assert calculate_grade(75, False) == "C"


def test_grade_D():
    assert calculate_grade(65, False) == "D"


def test_boundary_AB():
    assert calculate_grade(90, False) == "A"
    assert calculate_grade(89, False) == "B"


def test_boundary_BC():
    assert calculate_grade(80, False) == "B"
    assert calculate_grade(79, False) == "C"


def test_boundary_CD():
    assert calculate_grade(70, False) == "C"
    assert calculate_grade(69, False) == "D"


def test_boundary_DF():
    assert calculate_grade(60, False) == "D"
    assert calculate_grade(59, False) == "F"
