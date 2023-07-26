```python
import unittest
from src.affiliate_marketing import initiateAffiliateMarketing

class TestAffiliateMarketing(unittest.TestCase):

    def setUp(self):
        self.affiliatePartners = ['Amazon', 'eBay', 'Walmart']
        self.userProfileData = {
            'preferences': ['electronics', 'books'],
            'style': 'casual',
            'size': 'medium',
            'product_preferences': ['Samsung', 'Apple']
        }

    def test_initiateAffiliateMarketing(self):
        result = initiateAffiliateMarketing(self.userProfileData, self.affiliatePartners)
        self.assertIsInstance(result, dict)
        self.assertIn('affiliateLinks', result)
        self.assertIn('commissionRates', result)

        for partner in self.affiliatePartners:
            self.assertIn(partner, result['affiliateLinks'])
            self.assertIn(partner, result['commissionRates'])

if __name__ == '__main__':
    unittest.main()
```