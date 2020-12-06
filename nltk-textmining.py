# -*- coding: utf-8 -*-
"""

This code reads 2 text files of comments from the Pos and Con on the question:
    Should Recreational Marijuana Be Legal?
It finds the most common words and the most common bigrams.

"""

# importing the required libraries
from collections import Counter
import string

from nltk.corpus import sentiwordnet as swn
from nltk import pos_tag
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


# opening the files
Pos_file = open("pro_ marijuana_raw.txt","r", encoding='utf8')
Con_file = open("con_ marijuana_raw.txt","r", encoding='utf8')
stopwords_file = open("stopwords_en.txt","r", encoding='utf8')

# initializing the lists
stopwords = []
Pos_lines = []
Con_lines = []
Pos_words = []
Con_words = []

# loading the stopwords in a list
for s_word in stopwords_file:
    stopwords.append( s_word.strip() )
stopwords.extend (('marijuana', 'use', 'legal', 'year', 'years', 'cannabis'))
# the word marijuana has been added to the stopwords, being reasonably in most of the comments

# loading the "Pos" lines in a list
for p_line in Pos_file:
    if len(p_line) > 30:
        Pos_lines.append( p_line.strip() )

# loading the "against" lines in a list
for a_line in Con_file:
    if len(a_line) > 30:
        Con_lines.append( p_line.strip() )

# creating a list with the punctuation
exclude_punt = set(string.punctuation)

# Processing the "Pos" lines
for text_file1 in Pos_lines:
    parts = text_file1.strip().split()
    for word in parts:
        word = ''.join(ch for ch in word if ch not in exclude_punt)
        if word.lower() not in stopwords and len(word) > 2:
            Pos_words.append(word.lower())

# Poscessing the "against" lines
for text_file2 in Con_lines:
    parts = text_file2.strip().split()
    for word in parts:
        word = ''.join(ch for ch in word if ch not in exclude_punt)
        if word.lower() not in stopwords and len(word) > 2:
            Con_words.append(word.lower())

# calculating the top values
top_10_Pos = Counter(Pos_words).most_common(10)
top_10_Con = Counter(Con_words).most_common(10)

# printing the top values
print ("Top 10 Pos Words (Count):")
for pair in top_10_Pos:
    print (pair[0], "(" + str(pair[1]) + ")")

print ("\nTop 10 Con Words (Count):")
for pair in top_10_Con:
    print (pair[0], "(" + str(pair[1]) + ")")

##### BIGRAMS #####

# initializing the lists that will contain the bigrams
Pos_bigrams = []
Con_bigrams = []

# calculating the bigrams
for i in range(len(Pos_words)):
    try:
        Pos_bigrams.append( Pos_words[i] + "_" + Pos_words[i+1] )
    except:
        pass # reached end of list

for i in range(len(Con_words)):
    try:
        Con_bigrams.append( Con_words[i] + "_" + Con_words[i+1] )
    except:
        pass # reached end of list

# calculating the top values
common_Pos_bigrams = Counter(Pos_bigrams).most_common(5)
common_Con_bigrams = Counter(Con_bigrams).most_common(5)

# printing the top values
print ("\nCommon Con Bigrams:")
for i in range(5):
    bigram = common_Con_bigrams[i][0].split('_')
    print (bigram[0].title(), bigram[1].title())

print ("\nCommon Pos Bigrams:")
for i in range(5):
    bigram = common_Pos_bigrams[i][0].split('_')
    print (bigram[0].title(), bigram[1].title())
    
##### Sentiment Analysis #####

# tagging the words by part of speech
Pos_tagged = pos_tag(Pos_words)
Con_tagged = pos_tag(Con_words)


# calculating the sentiment components
Pos_pos_total = 0
Pos_neg_total = 0

Con_pos_total = 0
Con_neg_total = 0

for word in Pos_tagged:
    #print '\nword', word
    if word[1] == 'JJ':
        try:
            swn.senti_synset(word[0] + '.a.01').pos_score()
        except:
            continue
        #print '\nfor word -', word[0], '- the positive score is', swn.senti_synset(word[0] + '.a.01').pos_score()
        Pos_pos_total += swn.senti_synset(word[0] + '.a.01').pos_score()
        #print '   and the negative score is', swn.senti_synset(word[0] + '.a.01').neg_score()
        Pos_neg_total += swn.senti_synset(word[0] + '.a.01').neg_score()

print ('\nthe positive score for the pro marijuana comments is', Pos_pos_total)
print ('\nthe negative score for the pro marijuana comments is', Pos_neg_total)

for word in Con_tagged:
    if word[1] == 'JJ':
        try:
            swn.senti_synset(word[0] + '.a.01').pos_score()
        except:
            continue
        Con_pos_total += swn.senti_synset(word[0] + '.a.01').pos_score()
        Con_neg_total += swn.senti_synset(word[0] + '.a.01').neg_score()

print ('\nthe positive score for the con marijuana comments is', Con_pos_total)
print ('\nthe negative score for the con marijuana comments is', Con_neg_total)

##### Word cloud #####

# Transforming the lists of words into strings
Pos_words_strimg = ' '.join(Pos_words)
Con_words_strimg = ' '.join(Con_words)

# Creating and updating the stopword list
stpwords = set(STOPWORDS)
stpwords.add('people')
stpwords.add('legalization')
# words have been added to the stopwords, as samnple of removing words that are very frequent
#   to make room to others that are less obvious in the context

# Defining the wordcloud parameters
wc = WordCloud(background_color="white", max_words=2000,
               stopwords=stpwords)

# Generate word cloud
wc.generate(Pos_words_strimg)

# Store to file
#wc.to_file('Pos.png')

# Show the cloud
plt.imshow(wc)
plt.axis('off')
plt.show()
