```python
import unittest
from src.sponsored_product import promoteSponsoredProduct, SponsoredProductSchema

class TestSponsoredProduct(unittest.TestCase):

    def setUp(self):
        self.sponsored_product_data = {
            "product_id": "123",
            "brand": "BrandName",
            "category": "electronics",
            "price": 100.00,
            "description": "A great product",
            "image_url": "http://example.com/product.jpg"
        }

    def test_promote_sponsored_product(self):
        result = promoteSponsoredProduct(self.sponsored_product_data)
        self.assertTrue(result)

    def test_sponsored_product_schema(self):
        schema = SponsoredProductSchema()
        data, errors = schema.load(self.sponsored_product_data)
        self.assertFalse(errors)
        self.assertEqual(data, self.sponsored_product_data)

if __name__ == '__main__':
    unittest.main()
```