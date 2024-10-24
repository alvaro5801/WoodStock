import unittest
from entities.product import Product

class TestProduct(unittest.TestCase):
    def test_products_can_be_created(self):
        product = Product(name="random name", description="random description")
        self.assertIsInstance(product, Product)
        self.assertEqual(product.id, None)

    def test_products_cant_be_created_with_id(self):
        with self.assertRaises(TypeError):
            product = Product(id=1, name="random name", description="random description")
            return product
    