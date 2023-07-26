```python
import unittest
from src.recommendation_engine import generateRecommendations

class TestRecommendationEngine(unittest.TestCase):

    def setUp(self):
        self.userProfileData = {
            "preferences": ["electronics", "books"],
            "style": "modern",
            "size": "medium",
            "productPreferences": ["Samsung", "Apple"]
        }
        self.productData = [
            {"name": "Samsung Galaxy S21", "category": "electronics", "brand": "Samsung"},
            {"name": "Apple iPhone 12", "category": "electronics", "brand": "Apple"},
            {"name": "The Great Gatsby", "category": "books", "brand": "Penguin"}
        ]

    def test_generateRecommendations(self):
        recommendations = generateRecommendations(self.userProfileData, self.productData)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
        for product in recommendations:
            self.assertIn(product["category"], self.userProfileData["preferences"])
            self.assertIn(product["brand"], self.userProfileData["productPreferences"])

if __name__ == '__main__':
    unittest.main()
```