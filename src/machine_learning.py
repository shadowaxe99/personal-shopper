```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load user profile data and product data
userProfileData = pd.read_csv('userProfileData.csv')
productData = pd.read_csv('productData.csv')

def generateRecommendations(user_id):
    """
    Function to generate personalized product recommendations for a user
    """
    # Extract user's preferences
    user_preferences = userProfileData[userProfileData['user_id'] == user_id]['preferences'].values[0]

    # Create a TF-IDF matrix of product descriptions
    tfidf = TfidfVectorizer(stop_words='english')
    productData['description'] = productData['description'].fillna('')
    tfidf_matrix = tfidf.fit_transform(productData['description'])

    # Compute cosine similarity between user's preferences and product descriptions
    user_pref_vector = tfidf.transform([user_preferences])
    cosine_sim = cosine_similarity(user_pref_vector, tfidf_matrix)

    # Get top 10 product recommendations based on cosine similarity
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:10]

    product_indices = [i[0] for i in sim_scores]
    return productData.iloc[product_indices]
```