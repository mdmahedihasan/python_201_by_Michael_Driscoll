import mymath
import unittest


class TestAdd(unittest.TestCase):
    def test_add_integers(self):
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        result = mymath.add("abc", "def")
        self.assertEqual(result, "abcdef")


class TestSubtract(unittest.TestCase):
    def test_subtract_integers(self):
        result = mymath.subtract(10, 8)
        self.assertEqual(result, 2)


class TestMultiply(unittest.TestCase):
    def test_multiply_integers(self):
        result = mymath.multiply(5, 5)
        self.assertEqual(result, 25)


class TestDivide(unittest.TestCase):
    def test_divide_float(self):
        result = mymath.divide(10, 5)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = mymath.divide(8, 0)
            self.assertEqual(result, ZeroDivisionError)


if __name__ == '__main__':
    unittest.main()