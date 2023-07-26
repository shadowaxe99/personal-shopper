```python
import unittest
from src import nlp_processing

class TestNLPProcessing(unittest.TestCase):

    def setUp(self):
        self.sample_text = "This is a sample text for testing NLP processing."
        self.nlp_processor = nlp_processing.NLPProcessor()

    def test_tokenize(self):
        tokens = self.nlp_processor.tokenize(self.sample_text)
        self.assertEqual(tokens, ['This', 'is', 'a', 'sample', 'text', 'for', 'testing', 'NLP', 'processing.'])

    def test_remove_stopwords(self):
        text = "This is a sample text with some common stopwords."
        processed_text = self.nlp_processor.remove_stopwords(text)
        self.assertEqual(processed_text, "This sample text common stopwords.")

    def test_stemming(self):
        text = "This is a sample text with words that need stemming."
        stemmed_text = self.nlp_processor.stemming(text)
        self.assertEqual(stemmed_text, "This is a sampl text with word that need stem.")

    def test_lemmatization(self):
        text = "This is a sample text with words that need lemmatization."
        lemmatized_text = self.nlp_processor.lemmatization(text)
        self.assertEqual(lemmatized_text, "This is a sample text with word that need lemmatization.")

    def test_sentiment_analysis(self):
        text = "This is a great product!"
        sentiment = self.nlp_processor.sentiment_analysis(text)
        self.assertEqual(sentiment, 'Positive')

if __name__ == '__main__':
    unittest.main()
```