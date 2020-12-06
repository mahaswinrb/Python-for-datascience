# EM-624
# Exercise06

# This program will read three .dat files from the MovieLens data set (users, movies
# and ratings). Print the first 5 lines of each, then merge them into a single Pandas
# dataframe, replace occupation numbers with strings and print the last 5 lines of the 
# new dataframe. Bonus: Top 5 rating occupations

import pandas as pd

# Understand dataset
# data = pd.read_table('users.dat')
# print data
# 6038   6040::M::25::6::11106

# Set the column names and read each .dat file into a dataframe
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_csv('users.dat', sep='::', header=None, names=unames, engine='python') 

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('ratings.dat', sep='::', header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_csv('movies.dat', sep='::', header=None, names=mnames, engine='python')

# Print the first 5 lines of each
print('MovieLens Users:\n')
print(users[:5])
print('\n')
print('MovieLens Ratings:\n')
print(ratings[:5])
print('\n')
print('MovieLens Movies:\n')
print(movies[:5])
print('\n')

# Use 2 nested 'merge' functions to join all three dataframes into one
data = pd.merge(pd.merge(ratings, users), movies)

# Print the length of each data frame
print('Number of records in Users Dataframe: ',len(users.index))
print('Number of records in Ratings Dataframe: ',len(ratings.index))
print('Number of records in Movies Dataframe: ',len(movies.index))
print('Number of records in Overall Data Dataframe: ',len(data.index))

# Creat replacement dictionary for occupation column
replacements = {0: 'other/not specified',
                1: 'academic/educator',
                2: 'artist',
                3: 'clerical/admin',
                4: 'college/grad student',
                5: 'customer service',
                6: 'doctor/health care',
                7: 'executive/managerial',
                8: 'farmer',
                9: 'homemaker',
                10: 'K-12 student',
                11: 'lawyer',
                12: 'programmer',
                13: 'retired',
                14: 'sales/marketing',
                15: 'scientist',
                16: 'self-employed',
                17: 'technician/engineer',
                18: 'tradesman/craftsman',
                19: 'unemployed',
                20: 'writer'}

# Replace values using dictionary
data["occupation"].replace(replacements, inplace=True)

# Print last 5 rows of final dataframe
print('\n')
print('Movie Data:')
print('\n')
print(data[-5:])

#Bonus
print('\n')
print('Top Occupation Ratings:')
top = data.groupby(['occupation'])['rating'].mean()
print (top.sort_values(ascending=False)[:5])
