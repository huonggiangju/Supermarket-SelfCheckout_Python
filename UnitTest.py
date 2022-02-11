import unittest
#from Product import Product
import Product as p
from checkout import CheckoutRegister

#test product
class Test_Product(unittest.TestCase):

    def setUp(self):
        self.product = p.Product("P100", "Milk", "1 litre", 2.5)

    def test_Barcode(self):
        code = self.product.get_bar_code()
        self.assertEqual("123", code)

    def test_name(self):
        name = self.product.get_product_name()
        self.assertEqual("Milk", name)

    def test_desc(self):
        desc = self.product.get_product_desc()
        self.assertEqual("1 litre", desc)

    def test_price(self):
        price = self.product.get_product_price()
        self.assertEqual(2.5, price)

if __name__ == '__main__':
    unittest.main()
