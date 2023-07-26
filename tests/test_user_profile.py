```python
import unittest
from src import user_profile

class TestUserProfile(unittest.TestCase):

    def setUp(self):
        self.user_profile = user_profile.UserProfile()

    def test_create_user_profile(self):
        test_data = {
            "preferences": "Casual",
            "style": "Modern",
            "size": "M",
            "product_preferences": ["Jeans", "T-Shirts"]
        }
        result = self.user_profile.createUserProfile(test_data)
        self.assertEqual(result, True)

    def test_user_profile_data(self):
        test_data = {
            "preferences": "Casual",
            "style": "Modern",
            "size": "M",
            "product_preferences": ["Jeans", "T-Shirts"]
        }
        self.user_profile.createUserProfile(test_data)
        self.assertEqual(self.user_profile.userProfileData, test_data)

    def test_invalid_user_profile_data(self):
        test_data = {
            "preferences": "Casual",
            "style": "Modern",
            "size": "M",
            "product_preferences": ["Jeans", "T-Shirts"]
        }
        self.user_profile.createUserProfile(test_data)
        invalid_data = {
            "preferences": "Casual",
            "style": "Modern",
            "size": "M",
            "product_preferences": ["Jeans", "Shirts"]
        }
        self.assertNotEqual(self.user_profile.userProfileData, invalid_data)

if __name__ == '__main__':
    unittest.main()
```