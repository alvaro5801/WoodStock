import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_return_two(self):
        print(Product)
        prod = Product()
        self.assertEqual(2, prod.get_two)
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
if __name__ == '__main__':
    unittest.main()