```python
import pandas as pd
from datetime import datetime, timedelta

# Assuming we have a database connection established
from database_connection import DatabaseConnection

class UserRetentionMetrics:
    def __init__(self):
        self.db = DatabaseConnection()

    def calculate_user_retention(self):
        """
        Calculate the percentage of users who return to the app regularly.
        """
        # Get all user login data
        query = "SELECT user_id, login_date FROM user_login_data"
        login_data = pd.read_sql_query(query, self.db.connection)

        # Convert login_date to datetime
        login_data['login_date'] = pd.to_datetime(login_data['login_date'])

        # Get the date 30 days ago
        date_30_days_ago = datetime.now() - timedelta(days=30)

        # Filter users who have logged in within the last 30 days
        recent_users = login_data[login_data['login_date'] > date_30_days_ago]

        # Calculate the total number of users
        total_users = login_data['user_id'].nunique()

        # Calculate the number of recent users
        recent_users_count = recent_users['user_id'].nunique()

        # Calculate user retention rate
        user_retention_rate = (recent_users_count / total_users) * 100

        return user_retention_rate

if __name__ == "__main__":
    metrics = UserRetentionMetrics()
    print(f"User Retention Rate: {metrics.calculate_user_retention()}%")
```