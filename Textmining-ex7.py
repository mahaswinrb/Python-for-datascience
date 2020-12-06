# -*- coding: utf-8 -*-
"""

This code reads 1 text files, finds and prints the most common words and
    print/save the wordcloud.

"""

# Importing the required libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# reading input files
txt_file = open('Russian_agents.txt','r', encoding='utf8')
stopwords_file = open('stopwords_en.txt','r', encoding='utf8')

# initializing lists
stopwords = []
txt_words = []

# populating the list of stopwords
for word in stopwords_file:
    stopwords.append( word.strip() )

# updating the stopword list
stopwords.append('said')
stopwords.append('million')

# cleaning the text input file
for text_file, word_list in [(txt_file, txt_words)]:
    for line in text_file:
        parts = line.strip().split()
        for word in parts:
            if word.lower() not in stopwords:
                word_list.append(word.lower())

# Eliminate non alpha elements
text_list = [word.lower() for word in txt_words if word.isalpha()]

# calculating and printing the top 10 words
top_10_words = Counter(text_list).most_common(10)

print ('\nThe following are the top 10 words (Count):')
for pair in top_10_words:
    print (' -', pair[0], '(' + str(pair[1]) + ')')


##### WORDCLOUD #####
# transforming the list into a string for displaying
text_str = ' '.join(text_list)

# defining the wordcloud parameters
wc = WordCloud(background_color = 'white', max_words=2000)

# generating word cloud
wc.generate(text_str)

# storing to file
wc.to_file('txt.png')

# showing the cloud
plt.imshow(wc)
plt.axis('off')
plt.show()
