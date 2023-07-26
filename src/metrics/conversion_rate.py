```python
import pandas as pd

def calculate_conversion_rate(userProfileData, purchaseData):
    """
    Function to calculate the conversion rate of the app.
    Conversion rate is calculated as the number of users who made a purchase divided by the total number of users.
    """
    total_users = len(userProfileData)
    users_made_purchase = len(purchaseData[purchaseData['purchase'] == True])

    conversion_rate = (users_made_purchase / total_users) * 100

    return conversion_rate

def main():
    # Load user profile data
    userProfileData = pd.read_csv('data/userProfileData.csv')

    # Load purchase data
    purchaseData = pd.read_csv('data/purchaseData.csv')

    # Calculate conversion rate
    conversion_rate = calculate_conversion_rate(userProfileData, purchaseData)

    print(f"The conversion rate of the app is {conversion_rate}%")

if __name__ == "__main__":
    main()
```