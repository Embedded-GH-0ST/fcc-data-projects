import unittest
from main import arithmetic_arranger


class UnitTests(unittest.TestCase):
    def test_too_many_problems(self):
        actual = arithmetic_arranger(
            ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]
        )
        expected = "Error: Too many problems."
        self.assertEqual(
            actual,
            expected,
            'Expected calling "arithmetic_arranger()" with more than 5 problems to return "Error: Too many problems."',
        )

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(
            actual,
            expected,
            'Expected calling "arithmetic_arranger()" with an operator other than "+" or "-" to return "Error: Operator must be \'+\' or \'-\'."',
        )

    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(
            actual,
            expected,
            'Expected calling "arithmetic_arranger()" with numbers larger than 4 digits to return "Error: Numbers cannot be more than four digits."',
        )

    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(
            actual,
            expected,
            'Expected calling "arithmetic_arranger()" with numbers containing non-digits to return "Error: Numbers must only contain digits."',
        )

    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(
            actual, expected, "Expected checking the arrangement of the problems."
        )

    def test_solutions(self):
        actual = arithmetic_arranger(
            ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True
        )
        expected = "   32      3801      45      123\n+ 698    -    2    + 43    +  49\n-----    ------    ----    -----\n  730      3799      88      172"
        self.assertEqual(
            actual, expected, "Expected solutions to be correctly displayed."
        )


if __name__ == "__main__":
    unittest.main()
