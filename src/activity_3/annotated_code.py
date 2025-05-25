def calculate_grade(score, is_absent):
    grade = "F"  # d: definition of grade

    # p-use of is_absent
    if is_absent:
        grade = "I"  # d: redefinition of grade
    else:
        # p-use of score
        if score >= 90:  # p-use of score
            grade = "A"  # d: redefinition of grade
        elif score >= 80:  # p-use of score
            grade = "B"  # d: redefinition of grade
        elif score >= 70:  # p-use of score
            grade = "C"  # d: redefinition of grade
        elif score >= 60:  # p-use of score
            grade = "D"  # d: redefinition of grade

    # c-use of grade in return statement
    return grade
