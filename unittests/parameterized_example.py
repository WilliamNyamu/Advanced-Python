from parameterized import parameterized
import unittest

class TestMath(unittest.TestCase):
    def get_data():
        data = [
            (2, 3, 5),
            (10, 5, 15),
            (-2, -3, -5),
            (0, 0, 0)
        ]
        return data
    
    @parameterized.expand(get_data())
    def test_addition(self, a, b, expected):
        result = a + b
        self.assertEqual(result, expected)
    
    @parameterized.expand(get_data())
    def test_subtraction(self, a, b, expected):
        result = b - a
        self.assertEqual(result, expected)

if __name__=="__main__":
    unittest.main(verbosity=2)