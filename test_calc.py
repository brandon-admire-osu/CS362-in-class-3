import unittest

from calculator import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        for a, b in enumerate(range(1, 20, 2)):
            self.assertEqual(calc(int(a), int(b), "+"), a + b)

    def test_sub(self):
        for a, b in enumerate(range(1, 20, 2)):
            self.assertEqual(calc(int(a), int(b), "-"), a - b)

    def test_mult(self):
        for a, b in enumerate(range(1, 20, 2)):
            self.assertEqual(calc(int(a), int(b), "*"), a * b)

    def test_div(self):
        for a, b in enumerate(range(1, 20, 2)):
            self.assertEqual(calc(int(a), int(b), "/"), a / b)

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            calc("gun", 1, "+")
            calc(1, "gun", "+")
        with self.assertRaises(TypeError):
            calc(1, 2, 1)
            calc(1, 2, "gun")
            calc(1, 2, float)


if __name__ == "__main__":
    unittest.main()
