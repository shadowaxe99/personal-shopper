```python
import unittest
from src.metrics.conversion_rate import calculate_conversion_rate

class TestConversionRate(unittest.TestCase):

    def setUp(self):
        self.user_data = [
            {'user_id': 1, 'purchases': 5, 'product_views': 20},
            {'user_id': 2, 'purchases': 2, 'product_views': 10},
            {'user_id': 3, 'purchases': 0, 'product_views': 5},
            {'user_id': 4, 'purchases': 3, 'product_views': 15},
            {'user_id': 5, 'purchases': 1, 'product_views': 5}
        ]

    def test_calculate_conversion_rate(self):
        conversion_rate = calculate_conversion_rate(self.user_data)
        self.assertEqual(conversion_rate, 0.275)

if __name__ == '__main__':
    unittest.main()
```