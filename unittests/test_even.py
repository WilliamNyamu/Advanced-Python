import unittest
from even import even

class TestEven(unittest.TestCase):
    def test_even_number(self):
        for number in range(2, 10, 2):
            with self.subTest(number=number):
                self.assertEqual(even(number), True)
    
    def test_false_number(self):
        for number in range(1, 10, 2):
            with self.subTest(number=number):
                self.assertEqual(even(number), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)