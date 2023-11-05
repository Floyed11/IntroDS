from sklearn.feature_extraction.text import CountVectorizer

text = open('/Users/linto/Documents/IntroDaSE/Homework/IntroDS/chapter08/wordcloud.txt', encoding='utf-8').read()
text = [text]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)
print(X.toarray())
print(vectorizer.get_feature_names_out())