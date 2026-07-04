# Unittest - Python built-in testing framework
# Run: python -m unittest test_unittest.py

import unittest

# --- Functions to test ---
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(n):
    return n % 2 == 0

def get_user(user_id):
    users = {1: {"id": 1, "name": "Ajay"}, 2: {"id": 2, "name": "Ravi"}}
    return users.get(user_id)

# --- Test Class ---
class TestMathFunctions(unittest.TestCase):

    # setUp runs before each test
    def setUp(self):
        self.x = 10
        self.y = 5

    # Test methods must start with test_
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        self.assertFalse(is_even(3))

class TestUserFunctions(unittest.TestCase):

    def test_get_existing_user(self):
        user = get_user(1)
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], "Ajay")

    def test_get_missing_user(self):
        user = get_user(99)
        self.assertIsNone(user)

    def test_user_has_required_fields(self):
        user = get_user(1)
        self.assertIn("id", user)
        self.assertIn("name", user)

# --- Common Assertions ---
print("=== Common unittest Assertions ===")
assertions = {
    "assertEqual(a, b)":        "a == b",
    "assertNotEqual(a, b)":     "a != b",
    "assertTrue(x)":            "x is True",
    "assertFalse(x)":           "x is False",
    "assertIsNone(x)":          "x is None",
    "assertIsNotNone(x)":       "x is not None",
    "assertIn(a, b)":           "a in b",
    "assertRaises(Error, fn)":  "fn raises Error",
    "assertAlmostEqual(a, b)":  "a ≈ b (floats)",
}
for k, v in assertions.items():
    print(f"  {k:35}: {v}")

if __name__ == '__main__':
    unittest.main()
