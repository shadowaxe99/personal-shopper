```python
import unittest
from src.wishlist_favorites import addToWishlist, markAsFavorite

class TestWishlistFavorites(unittest.TestCase):

    def setUp(self):
        self.userProfileData = {
            "userId": 1,
            "preferences": ["casual", "sporty"],
            "size": "M",
            "productPreferences": ["shoes", "shirts"]
        }
        self.productData = {
            "productId": 101,
            "name": "Running Shoes",
            "category": "shoes",
            "price": 100,
            "size": ["S", "M", "L"],
            "style": ["sporty"]
        }

    def test_addToWishlist(self):
        result = addToWishlist(self.userProfileData["userId"], self.productData["productId"])
        self.assertEqual(result, {"status": "success", "message": "Product added to wishlist"})

    def test_markAsFavorite(self):
        result = markAsFavorite(self.userProfileData["userId"], self.productData["productId"])
        self.assertEqual(result, {"status": "success", "message": "Product marked as favorite"})

if __name__ == '__main__':
    unittest.main()
```