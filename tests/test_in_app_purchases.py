```python
import unittest
from src import in_app_purchases

class TestInAppPurchases(unittest.TestCase):

    def setUp(self):
        self.purchase = in_app_purchases.makeInAppPurchase()

    def test_purchase_success(self):
        self.assertEqual(self.purchase.purchaseConfirmationMessage, "Purchase successful!")

    def test_purchase_failure(self):
        self.purchase.productData = None
        self.assertEqual(self.purchase.purchaseConfirmationMessage, "Purchase failed. Please try again.")

    def test_purchase_product_not_found(self):
        self.purchase.productData = {"product_id": "123", "product_name": "Non-existent product"}
        self.assertEqual(self.purchase.purchaseConfirmationMessage, "Product not found. Please try again.")

    def test_purchase_insufficient_funds(self):
        self.purchase.userProfileData = {"user_id": "1", "balance": 0}
        self.assertEqual(self.purchase.purchaseConfirmationMessage, "Insufficient funds. Please top up your balance.")

if __name__ == '__main__':
    unittest.main()
```