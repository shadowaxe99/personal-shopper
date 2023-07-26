```python
import unittest
from src.premium_features import offerPremiumFeatures, PremiumSchema

class TestPremiumFeatures(unittest.TestCase):

    def setUp(self):
        self.premiumFeatures = [
            {
                "name": "Ad-free browsing",
                "description": "Enjoy an ad-free shopping experience",
                "price": 5.99
            },
            {
                "name": "Early access to sales",
                "description": "Get early access to our biggest sales",
                "price": 9.99
            }
        ]

    def test_offerPremiumFeatures(self):
        result = offerPremiumFeatures(self.premiumFeatures)
        self.assertIsInstance(result, list)
        for feature in result:
            self.assertIsInstance(feature, dict)
            self.assertTrue(PremiumSchema.validate(feature))

if __name__ == '__main__':
    unittest.main()
```