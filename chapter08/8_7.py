from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

data = fetch_20newsgroups()
tfidf = TfidfVectorizer()
X= tfidf.fit_transform(data.data)

print(X[0])