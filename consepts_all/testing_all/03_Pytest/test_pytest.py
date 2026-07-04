# Pytest - Most popular Python testing framework
# pip install pytest pytest-cov
# Run: pytest test_pytest.py -v
# Run all: pytest
# With coverage: pytest --cov=. --cov-report=term

import pytest

# --- Functions to test ---
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, qty=1):
        self.items.append({"name": name, "price": price, "qty": qty})

    def total(self):
        return sum(i["price"] * i["qty"] for i in self.items)

    def remove_item(self, name):
        self.items = [i for i in self.items if i["name"] != name]

    def is_empty(self):
        return len(self.items) == 0

# --- Simple tests (no class needed in pytest) ---
def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# --- Fixtures (reusable test setup) ---
@pytest.fixture
def cart():
    c = ShoppingCart()
    c.add_item("Laptop", 50000)
    c.add_item("Phone", 20000, qty=2)
    return c

def test_cart_total(cart):
    assert cart.total() == 90000  # 50000 + 20000*2

def test_cart_not_empty(cart):
    assert not cart.is_empty()

def test_cart_remove_item(cart):
    cart.remove_item("Phone")
    assert cart.total() == 50000

def test_empty_cart():
    c = ShoppingCart()
    assert c.is_empty()
    assert c.total() == 0

# --- Parametrize (run same test with multiple inputs) ---
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected

# --- Skip and xfail ---
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert add(1, 1) == 3  # will fail but marked as expected

# Run: pytest test_pytest.py -v
