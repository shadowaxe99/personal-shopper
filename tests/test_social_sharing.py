```python
import unittest
from unittest.mock import patch
from src.social_sharing import shareOnSocialMedia

class TestSocialSharing(unittest.TestCase):

    @patch('src.social_sharing.shareOnSocialMedia')
    def test_shareOnSocialMedia(self, mock_share):
        # Mock user profile data
        userProfileData = {
            'username': 'test_user',
            'preferences': {
                'style': 'casual',
                'size': 'M',
                'product_preferences': ['shoes', 'shirts']
            }
        }

        # Mock product data
        productData = {
            'id': '123',
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': 100,
            'features': ['feature1', 'feature2']
        }

        # Call the function with mock data
        shareOnSocialMedia(userProfileData, productData)

        # Assert the function was called with correct arguments
        mock_share.assert_called_with(userProfileData, productData)

if __name__ == '__main__':
    unittest.main()
```