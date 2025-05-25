def max_of_three_numbers(a: int, b: int, c: int) -> int:
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c
