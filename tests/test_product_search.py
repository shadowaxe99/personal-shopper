```python
import unittest
from src.product_search import searchProduct, compareProducts

class TestProductSearch(unittest.TestCase):

    def setUp(self):
        self.productData = [
            {"id": 1, "name": "Product 1", "price": 100, "features": "Feature 1, Feature 2"},
            {"id": 2, "name": "Product 2", "price": 200, "features": "Feature 3, Feature 4"},
            {"id": 3, "name": "Product 3", "price": 150, "features": "Feature 5, Feature 6"}
        ]

    def test_searchProduct(self):
        result = searchProduct("Product 1", self.productData)
        self.assertEqual(result, self.productData[0])

        result = searchProduct("Product 4", self.productData)
        self.assertIsNone(result)

    def test_compareProducts(self):
        result = compareProducts("Product 1", "Product 2", self.productData)
        self.assertEqual(result, {"Product 1": self.productData[0], "Product 2": self.productData[1]})

        result = compareProducts("Product 1", "Product 4", self.productData)
        self.assertEqual(result, {"Product 1": self.productData[0], "Product 4": None})

if __name__ == '__main__':
    unittest.main()
```