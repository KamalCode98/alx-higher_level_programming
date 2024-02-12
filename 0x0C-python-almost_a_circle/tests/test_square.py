import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def setUp(self):
        """Set up test fixtures."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    # Tests for constructor
    def test_constructor_no_args(self):
        """Test constructor with no arguments."""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_constructor_many_args(self):
        """Test constructor with too many arguments."""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_constructor_one_args(self):
        """Test constructor with only one argument."""
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_instantiation(self):
        """Test instantiation and attribute values."""
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)

        # Test more instantiation scenarios...

    # Tests for area method
    def test_area(self):
        """Test area() method."""
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

        # Test more scenarios for area()...

    # Tests for display method
    def test_display_no_args(self):
        """Test display() method signature."""
        r = Rectangle(9, 8)
        with self.assertRaises(TypeError):
            r.display()

    def test_display_simple(self):
        """Test display() method output."""
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "#\n")

        # Test more scenarios for display()...

    # Tests for __str__ method
    def test_str_no_args(self):
        """Test __str__() method signature."""
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError):
            Rectangle.__str__()

    def test_str(self):
        """Test __str__() method return."""
        r = Rectangle(5, 2)
        self.assertEqual(str(r), '[Rectangle] (1) 0/0 - 5/2')

        # Test more scenarios for __str__()...

    # Add more test methods for other functionalities...


if __name__ == "__main__":
    unittest.main()
