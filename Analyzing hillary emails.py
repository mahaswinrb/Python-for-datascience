# -*- coding: utf-8 -*-
# The script analyses the Hillary Clinton's emails released by FBI


# importing libraries   
import csv
import string
from bokeh.plotting import output_file, show, figure
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

print ('\nStarting the process...')

#reading input file, with emails and load them into a dictionary
file_clinton=open('H_Clinton-emails.csv', encoding='utf8')
reader = csv.DictReader(file_clinton)

'''
loading the data into a dictionary. Please note:
    When you define two variables in a for loop in conjunction with a call to items() on a dictionary,
    Python automatically assigns the first variable as the name of a key in that dictionary,
    and the second variable as the corresponding value for that key
'''

data_in = {}
for row in reader:
    for header, value in row.items():
        try:
            data_in[header].append(value)
        except KeyError:
            data_in[header] = [value]

# creating variables with list of senders and words
source_from = data_in['MetadataFrom'] 
source_words = data_in['RawText']

# reading the stopwords file and adding more stopwords in a new list
stopwords = open('stopwords_en.txt', encoding='utf8')
Stopword_list=[]
Stopwords_extension = ['clinton', 'u.s.', 'amto:','unclassified','sent:','srom:','subject:','to:', 'from:', 'cc:', 're:', 'years',
    'i','f-2014-20439','date:','no.','j','c','-', 'w', 'tO','a','for',':',';','2011','2012','2013','2014', '-', '2015',
    'r','07/31/2011','—','08/31/2015','in','and','pm','on','no','he','new','','it','the','pir','07/31/2015','am', 'foia', 'f201504841',
    'b6','06/30/2015','2010','2009','a','-','--','cc:','h','we','fw:','in','d', 'f201420439', '\x0cunclassified', '\xe2\x80\xa2']
for words in stopwords:
   Stopword_list.append(words.strip().lower())
Stopword_list.extend(Stopwords_extension)

# initializing the lists of senders and words
Senders_list=[]
RawText_list=[]

# populating the list of senders
for send in source_from:
        new = send.strip().split("\n")
        for w in new:
            clean_w1 = w.lower().translate(string.punctuation)
            if clean_w1 not in Stopword_list:
                Senders_list.append(clean_w1)

# populating the list of words
for words in source_words:
    new_w = words.strip().split(" ")
    for words in new_w:
        new = words.strip().split("\n")
        for w in new:
            clean_w2 = w.lower().translate(string.punctuation)
            if clean_w2 not in Stopword_list:
                if clean_w2.isdigit():
                    continue
                RawText_list.append(clean_w2)                       

# counter1 contains a list of couples (sender, frequency)
counter1 = Counter(Senders_list).most_common(10)

# counter2 contains a list of couples (word, frequency)
counter2 = Counter(RawText_list).most_common(50)
#print counter2

# initializing the lists containing the elements to display and plot
list_from = []
list_from_num = []
list_words = []
list_words_num = []

# creating and printing the list of most common senders
print ('\nMost common senders:')
for pair1 in counter1:
   list_from.append (pair1[0])       
   list_from_num.append (pair1[1])       
   print (pair1[0],str(pair1[1]))     

# creating and printing the list of most common words
print ('\nMost common words:')
for pair2 in counter2:
    list_words.append (pair2[0])
    list_words_num.append (pair2[1])       
    print (pair2[0],str(pair2[1]))

# creating the graphs
print ('\nNow creating the graphs...\n')

# first graph - WordCloud
str_words = ' '.join(list_words)
wcloud = WordCloud(background_color = 'white',max_words = 2000)
wcloud.generate(str_words)
wcloud.to_file('words.png')
plt.imshow(wcloud)
plt.axis('off')
plt.show()
print ('WordCloud generated\n')


# second graph - Senders
bar_chart1 = figure(x_range = list_from, plot_width = 800, plot_height = 600, title = 'Frequency of senders')
bar_chart1.vbar (x = list_from, top = list_from_num, width = 0.5)
bar_chart1.xaxis.major_label_orientation = 1.2
output_file('Sender_names.html')
show(bar_chart1)
print ('Senders bar chart generated\n')

# third graph - Words
bar_chart2 = figure(x_range = list_words, plot_width = 800, plot_height = 600, title = 'Frequency of words')
bar_chart2.vbar (x = list_words, top = list_words_num, width = 0.5)
bar_chart2.xaxis.major_label_orientation = 1.2
output_file('Frequent_words.html')
show(bar_chart2)
print ('Words bar chart generated\n')

print ('\nEnd of process!\n')



