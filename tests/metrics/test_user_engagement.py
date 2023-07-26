```python
import unittest
from src.metrics.user_engagement import UserEngagement

class TestUserEngagement(unittest.TestCase):

    def setUp(self):
        self.user_engagement = UserEngagement()

    def test_time_spent(self):
        time_spent = self.user_engagement.calculate_time_spent()
        self.assertIsInstance(time_spent, float)
        self.assertGreaterEqual(time_spent, 0)

    def test_product_views(self):
        product_views = self.user_engagement.calculate_product_views()
        self.assertIsInstance(product_views, int)
        self.assertGreaterEqual(product_views, 0)

    def test_click_through_rate(self):
        click_through_rate = self.user_engagement.calculate_click_through_rate()
        self.assertIsInstance(click_through_rate, float)
        self.assertGreaterEqual(click_through_rate, 0)
        self.assertLessEqual(click_through_rate, 1)

if __name__ == '__main__':
    unittest.main()
```