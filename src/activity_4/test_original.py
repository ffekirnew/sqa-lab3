import unittest

from src.activity_4.original import calculate_absolute_difference


class TestAbsoluteDifference(unittest.TestCase):
    def test_case_1_a_greater_than_b(self):
        # Test when a is greater than b
        self.assertEqual(calculate_absolute_difference(10, 5), 5)

    def test_case_2_b_greater_than_a(self):
        # Test when b is greater than a
        self.assertEqual(calculate_absolute_difference(3, 7), 4)

    def test_case_3_a_equals_b(self):
        # Test when a equals b
        self.assertEqual(calculate_absolute_difference(8, 8), 0)

    def test_case_4_negative_numbers(self):
        # Test with negative numbers
        self.assertEqual(calculate_absolute_difference(-5, -10), 5)

    def test_case_5_mixed_numbers(self):
        # Test with mixed positive and negative numbers
        self.assertEqual(calculate_absolute_difference(5, -5), 10)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
