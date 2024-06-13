import unittest
from FIND_BY_NAME.models import Product  # Adjust the import to your project's structure
from FIND_BY_NAME import db

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Set up a test database or any required initial state
        db.create_all()  # Ensure the database and tables are created
        self.product = Product(name="Test Product", description="This is a test product", price=9.99, stock=10)
        db.session.add(self.product)
        db.session.commit()

    def tearDown(self):
        # Clean up the database after each test
        db.session.remove()
        db.drop_all()

    def test_find_by_name(self):
        # Find the product by name in the database
        product = Product.query.filter_by(name="Test Product").first()
        self.assertIsNotNone(product)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "This is a test product")
        self.assertEqual(product.price, 9.99)
        self.assertEqual(product.stock, 10)

if __name__ == "__main__":
    unittest.main()
