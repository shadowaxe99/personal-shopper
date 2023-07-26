```python
import unittest
from src.machine_learning import generateRecommendations

class TestMachineLearning(unittest.TestCase):

    def setUp(self):
        self.userProfileData = {
            "preferences": ["electronics", "books"],
            "style": "casual",
            "size": "medium",
            "productPreferences": ["brandA", "brandB"]
        }
        self.productData = [
            {"name": "product1", "category": "electronics", "brand": "brandA"},
            {"name": "product2", "category": "books", "brand": "brandB"},
            {"name": "product3", "category": "clothing", "brand": "brandC"}
        ]

    def test_generateRecommendations(self):
        recommendations = generateRecommendations(self.userProfileData, self.productData)
        self.assertIsInstance(recommendations, list)
        for product in recommendations:
            self.assertIn(product["category"], self.userProfileData["preferences"])
            self.assertIn(product["brand"], self.userProfileData["productPreferences"])

if __name__ == '__main__':
    unittest.main()
```