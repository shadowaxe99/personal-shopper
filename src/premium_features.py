```python
from src.user_profile import UserProfileSchema
from src.backend_infrastructure import Database

class PremiumFeatures:
    def __init__(self):
        self.db = Database()
        self.premiumFeatures = []

    def load_premium_features(self):
        self.premiumFeatures = self.db.get_all("premiumFeatures")

    def offer_premium_features(self, user_id):
        user_profile = self.db.get_one("userProfileData", {"_id": user_id})
        if not user_profile:
            raise Exception("User not found")

        user_profile_schema = UserProfileSchema(**user_profile)
        for feature in self.premiumFeatures:
            if feature["category"] in user_profile_schema.preferences:
                yield feature

    def subscribe_user(self, user_id, feature_id):
        user_profile = self.db.get_one("userProfileData", {"_id": user_id})
        if not user_profile:
            raise Exception("User not found")

        feature = self.db.get_one("premiumFeatures", {"_id": feature_id})
        if not feature:
            raise Exception("Feature not found")

        if "subscriptions" not in user_profile:
            user_profile["subscriptions"] = []

        user_profile["subscriptions"].append(feature_id)
        self.db.update_one("userProfileData", {"_id": user_id}, user_profile)

    def unsubscribe_user(self, user_id, feature_id):
        user_profile = self.db.get_one("userProfileData", {"_id": user_id})
        if not user_profile:
            raise Exception("User not found")

        if "subscriptions" not in user_profile or feature_id not in user_profile["subscriptions"]:
            raise Exception("User not subscribed to this feature")

        user_profile["subscriptions"].remove(feature_id)
        self.db.update_one("userProfileData", {"_id": user_id}, user_profile)
```