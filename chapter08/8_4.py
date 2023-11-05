from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

stopwords = '的 了 是 有 个 人 在 也 和 与 中 为 以 这 之 但 并 于'.split()
mask = np.array(Image.open('/Users/linto/Documents/IntroDaSE/Homework/IntroDS/chapter08/wordcloud.png'))
text = open('/Users/linto/Documents/IntroDaSE/Homework/IntroDS/chapter08/wordcloud.txt', encoding='utf-8').read()

wc = WordCloud(max_words = 1000, mask = mask, stopwords = stopwords, margin = 10, random_state = 1).generate(text)
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()