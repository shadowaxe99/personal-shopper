```python
import datetime
from src.user_profile import userProfileData
from src.product_search import productData

class UserEngagementMetrics:
    def __init__(self):
        self.user_engagement_data = {}

    def track_time_spent(self, user_id, start_time, end_time):
        time_spent = end_time - start_time
        if user_id in self.user_engagement_data:
            self.user_engagement_data[user_id]['time_spent'] += time_spent
        else:
            self.user_engagement_data[user_id] = {'time_spent': time_spent}

    def track_product_views(self, user_id, product_id):
        if user_id in self.user_engagement_data:
            if 'product_views' in self.user_engagement_data[user_id]:
                self.user_engagement_data[user_id]['product_views'].append(product_id)
            else:
                self.user_engagement_data[user_id]['product_views'] = [product_id]
        else:
            self.user_engagement_data[user_id] = {'product_views': [product_id]}

    def track_click_through_rate(self, user_id, clicked, viewed):
        if user_id in self.user_engagement_data:
            if 'click_through_rate' in self.user_engagement_data[user_id]:
                self.user_engagement_data[user_id]['click_through_rate']['clicked'] += clicked
                self.user_engagement_data[user_id]['click_through_rate']['viewed'] += viewed
            else:
                self.user_engagement_data[user_id]['click_through_rate'] = {'clicked': clicked, 'viewed': viewed}
        else:
            self.user_engagement_data[user_id] = {'click_through_rate': {'clicked': clicked, 'viewed': viewed}}

    def calculate_click_through_rate(self, user_id):
        if user_id in self.user_engagement_data and 'click_through_rate' in self.user_engagement_data[user_id]:
            clicked = self.user_engagement_data[user_id]['click_through_rate']['clicked']
            viewed = self.user_engagement_data[user_id]['click_through_rate']['viewed']
            if viewed != 0:
                return clicked / viewed
            else:
                return 0
        else:
            return 0

    def get_user_engagement_data(self, user_id):
        if user_id in self.user_engagement_data:
            return self.user_engagement_data[user_id]
        else:
            return None
```