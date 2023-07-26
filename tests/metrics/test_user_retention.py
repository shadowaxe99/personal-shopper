```python
import unittest
from src.metrics.user_retention import calculate_user_retention

class TestUserRetention(unittest.TestCase):

    def setUp(self):
        self.userProfileData = [
            {"user_id": 1, "last_login": "2022-01-01"},
            {"user_id": 2, "last_login": "2022-01-15"},
            {"user_id": 3, "last_login": "2022-02-01"},
            {"user_id": 4, "last_login": "2022-02-15"},
            {"user_id": 5, "last_login": "2022-03-01"}
        ]

    def test_calculate_user_retention(self):
        retention_rate = calculate_user_retention(self.userProfileData, "2022-03-01")
        self.assertEqual(retention_rate, 0.6)

if __name__ == '__main__':
    unittest.main()
```