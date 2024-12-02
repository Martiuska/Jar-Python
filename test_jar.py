# pytest to test the code I created in a file .py
# It is used not to work on all the code everytime
# * is for comprehension
# Why should we add _ for emissions_per_unit?

# To improve it I will change the code on .py (for example with approximation)


import pytest

from jar import Jar  # Import the Jar class from jar.py

def test_init():
    """Test initializing the Jar class."""
    jar = Jar(10)
    assert jar.capacity == 10  # Check if capacity is set correctly
    assert jar.size == 0  # Check if initial size is 0

def test_deposit():
    """Test depositing cookies into the jar."""
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3  # After depositing 3 cookies, size should be 3

    # Test exceeding capacity
    try:
        jar.deposit(3)
    except ValueError as e:
        assert str(e) == "Cannot add more cookies than the jar's capacity."

def test_withdraw():
    """Test withdrawing cookies from the jar."""
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2  # After withdrawing 3 cookies, size should be 2

    # Test withdrawing more than available
    try:
        jar.withdraw(3)
    except ValueError as e:
        assert str(e) == "Cannot remove more cookies than are in the jar."

def test_str():
    """Test the string representation of the jar."""
    jar = Jar(4)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"  # Check if the string matches the number of cookies