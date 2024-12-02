class Jar:
    def __init__(self, capacity=12):
        """
        Initialize the cookie jar with a given capacity.
        Capacity must be a non-negative integer. If not, raise a ValueError.
        """
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity  # The maximum number of cookies the jar can hold
        self._cookies = 0  # Initially, the jar is empty

    def __str__(self):
        """
        Return a string representing the cookies in the jar.
        Each cookie is represented by the 🍪 emoji.
        """
        return "🍪" * self._cookies

    def deposit(self, n):
        """
        Add n cookies to the jar.
        If adding n cookies exceeds the jar's capacity, raise a ValueError.
        """
        if self._cookies + n > self._capacity:
            raise ValueError("Cannot add more cookies than the jar's capacity.")
        self._cookies += n  # Increase the number of cookies in the jar

    def withdraw(self, n):
        """
        Remove n cookies from the jar.
        If there are not enough cookies in the jar, raise a ValueError.
        """
        if n > self._cookies:
            raise ValueError("Cannot remove more cookies than are in the jar.")
        self._cookies -= n  # Decrease the number of cookies in the jar

    @property
    def capacity(self):
        """
        Return the maximum capacity of the jar.
        """
        return self._capacity

    @property
    def size(self):
        """
        Return the current number of cookies in the jar.
        """
        return self._cookies

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