```python
from src.user_profile import UserProfileSchema
from src.product_search import ProductSchema

wishlistData = []
favoritesData = []

class WishlistSchema:
    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

class FavoritesSchema:
    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

def addToWishlist(user_id, product_id):
    new_item = WishlistSchema(user_id, product_id)
    wishlistData.append(new_item)
    return "Item added to wishlist successfully."

def removeFromWishlist(user_id, product_id):
    for item in wishlistData:
        if item.user_id == user_id and item.product_id == product_id:
            wishlistData.remove(item)
            return "Item removed from wishlist successfully."
    return "Item not found in wishlist."

def markAsFavorite(user_id, product_id):
    new_item = FavoritesSchema(user_id, product_id)
    favoritesData.append(new_item)
    return "Item marked as favorite successfully."

def unmarkAsFavorite(user_id, product_id):
    for item in favoritesData:
        if item.user_id == user_id and item.product_id == product_id:
            favoritesData.remove(item)
            return "Item unmarked as favorite successfully."
    return "Item not found in favorites."
```