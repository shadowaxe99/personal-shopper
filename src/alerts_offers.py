```python
import time
from src.user_profile import userProfileData
from src.product_search import productData

# Function to check for price drops and special offers
def check_for_alerts():
    alerts = []
    for product in productData:
        if product['price_drop'] or product['special_offer']:
            alerts.append(product)
    return alerts

# Function to send real-time alerts and offers
def sendAlerts():
    alerts = check_for_alerts()
    for user in userProfileData:
        user_alerts = [alert for alert in alerts if alert['product_id'] in user['product_preferences']]
        if user_alerts:
            user['alerts'] = user_alerts
            print(f"Alert message for {user['username']}: {alertMessage}")
            time.sleep(1)  # simulate delay

# Function to check for deals on products of interest
def check_for_deals():
    deals = []
    for product in productData:
        if product['deal']:
            deals.append(product)
    return deals

# Function to send deals on products of interest
def sendDeals():
    deals = check_for_deals()
    for user in userProfileData:
        user_deals = [deal for deal in deals if deal['product_id'] in user['product_preferences']]
        if user_deals:
            user['deals'] = user_deals
            print(f"Deal message for {user['username']}: {alertMessage}")
            time.sleep(1)  # simulate delay

if __name__ == "__main__":
    sendAlerts()
    sendDeals()
```