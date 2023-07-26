```python
import unittest
from src.alerts_offers import sendAlerts

class TestAlertsOffers(unittest.TestCase):

    def setUp(self):
        self.userProfileData = {
            "preferences": ["electronics", "books"],
            "style": "casual",
            "size": "medium",
            "productPreferences": ["Samsung", "Apple"]
        }
        self.productData = [
            {
                "name": "Samsung Galaxy S21",
                "category": "electronics",
                "price": 799.99,
                "brand": "Samsung"
            },
            {
                "name": "Apple iPhone 12",
                "category": "electronics",
                "price": 699.99,
                "brand": "Apple"
            },
            {
                "name": "The Great Gatsby",
                "category": "books",
                "price": 9.99,
                "brand": "Scribner"
            }
        ]

    def test_send_alerts(self):
        alerts = sendAlerts(self.userProfileData, self.productData)
        self.assertIsInstance(alerts, list)
        self.assertGreater(len(alerts), 0)
        for alert in alerts:
            self.assertIn(alert['category'], self.userProfileData['preferences'])
            self.assertIn(alert['brand'], self.userProfileData['productPreferences'])

if __name__ == '__main__':
    unittest.main()
```