import unittest
from models import Product, Session


class TestProductOperations(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.session = Session()

    def tearDown(self):
        self.transaction.rollback()
        self.session.close()

    def test_adding_product(self):
        # create a new product
        new_product = Product(name="test product", price=20.50)
        self.session.add(new_product)
        self.session.commit()

        added_product = self.session.query(Product).filter_by(name="test product").first()
        self.assertIsNotNone(added_product)
        self.assertEqual(added_product.price, 20.50)

    def test_reading_product(self):
        product = Product(name="read product", price=17.80)
        self.session.add(product)
        self.session.commit()

        retrieved_product = self.session.query(Product).filter_by(name="Read Product").first()
        self.assertEqual(retrieved_product.name, "Read Product")

    def test_updating_product(self):
        product = Product(name="update product", price=30.00)
        self.session.add(product)
        self.session.commit()

        product.price = 25.50
        self.session.commit()

        updated_product = self.session.query(Product).filter_by(name="update product").first()
        self.assertEqual(updated_product.price, 25.50)

    def test_deleting_product(self):
        product = Product(name="delete product", price=8.90)
        self.session.add(product)
        self.session.commit()

        self.session.delete(product)
        self.session.commit()

        deleted_product = self.session.query(Product).filter_by(name="delete product").first()
        self.assertIsNone(deleted_product)


if __name__ == '__main__':
    unittest.main()
