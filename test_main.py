from main import quadratic_multiply, BinaryNumber
import unittest

class TestQuadraticMultiply(unittest.TestCase):
    def test_multiply_basic(self):
        # Test basic multiplication
        self.assertEqual(quadratic_multiply(BinaryNumber(3), BinaryNumber(3)), 9, "3*3 should be 9")

    def test_multiply_zero(self):
        # Test multiplication by zero
        self.assertEqual(quadratic_multiply(BinaryNumber(0), BinaryNumber(5)), 0, "0*5 should be 0")
        self.assertEqual(quadratic_multiply(BinaryNumber(5), BinaryNumber(0)), 0, "5*0 should be 0")

    def test_multiply_one(self):
        # Test multiplication by one
        self.assertEqual(quadratic_multiply(BinaryNumber(1), BinaryNumber(5)), 5, "1*5 should be 5")
        self.assertEqual(quadratic_multiply(BinaryNumber(5), BinaryNumber(1)), 5, "5*1 should be 5")

    def test_multiply_large_numbers(self):
        # Test multiplication of large numbers
        self.assertEqual(quadratic_multiply(BinaryNumber(1234), BinaryNumber(5678)), 1234*5678, "1234*5678 should be correct")

    def test_multiply_odd_length(self):
        # Test multiplication where numbers have odd lengths
        self.assertEqual(quadratic_multiply(BinaryNumber(123), BinaryNumber(45)), 123*45, "123*45 should be correct")

    def test_multiply_even_length(self):
        # Test multiplication where numbers have even lengths
        self.assertEqual(quadratic_multiply(BinaryNumber(1234), BinaryNumber(5678)), 1234*5678, "1234*5678 should be correct")

if __name__ == '__main__':
    unittest.main()
