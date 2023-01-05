from nltk.tokenize import WordPunctTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


class CleaningMixin:
    def deep_clean(self, value):
        value = str(value).replace('\n', '')
        value = str(value).replace('\r', '')
        tokens = value.split('')
        result = ' '.join(filter(lambda x: x != '', tokens))
        return result

    def clean(self, value):
        value = value.strip()
        return self.deep_clean(value)


class TextMachineLearning:
    """Dectect the probability for 
    a group of text to contain a certain
    specific set of words"""
    vocabulary = {}
    vector = None

    def normalize(self, text):
        instance = WordPunctTokenizer()
        tokens = instance.tokenize(text)
        result1 = filter(lambda x: x != '', tokens)
        result2 = map(lambda x: x.lower().strip(), result1)
        return ' '.join(result2)

    def analyze(self, text):
        text = self.normalize(text)
        # Create a vocabulary of known words
        # and tokenize the document
        count_vectorizer = CountVectorizer(stop_words=None)
        count_vectorizer.fit(text)
        self.vector = count_vectorizer.transform(text)
        self.vocabulary = count_vectorizer.vocabulary_
