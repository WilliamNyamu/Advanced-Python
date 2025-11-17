import unittest
from prime_v1 import is_prime

class TestPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(is_prime(9), False)


if __name__=="__main__":
    unittest.main()

