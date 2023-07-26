```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        # Tokenization
        word_tokens = word_tokenize(text)

        # Stopwords removal
        filtered_sentence = [w for w in word_tokens if not w in self.stop_words]

        # Lemmatization
        lemmatized_sentence = [self.lemmatizer.lemmatize(w) for w in filtered_sentence]

        return lemmatized_sentence

nlp_processor = NLPProcessor()

def process_user_preferences(userProfileData):
    processed_preferences = {}
    for key, value in userProfileData.items():
        processed_preferences[key] = nlp_processor.preprocess_text(value)
    return processed_preferences

def process_product_data(productData):
    processed_products = {}
    for key, value in productData.items():
        processed_products[key] = nlp_processor.preprocess_text(value)
    return processed_products
```