'''
 Author:  ---

 Exercise 00.5
 Sample progam

 This program read a file with US baby names and

1. Print the data structure info
2. Delete the column 'Unnamed: 0' and 'Id'
3. Determine if there are more gender "F" or "M"
4. Print the top 5 in terms of number of occurrences per name
5. Print the number of names in the dataset
6. Print the standard deviation of name occurrence
7. Print the basic descriptive statistics on the dataset

'''

# importing a function to create some of the lists of validation character
import pandas as pd

# reading the file into a pandas structure
baby_names = pd.read_csv('US_Baby_Names_right.csv')

# printing the data structure info
print ('\nthis is the raw data structure')
print (baby_names.info())

# deleting the column "Unnamed: 0"
del baby_names['Unnamed: 0']
# deleting the column "id"
del baby_names['Id']

# printing the first 10 names in the new data structure
print ('\nthis are the 1st names in the new structure')
print (baby_names.head(10))

print ('\nthe following is the distribution between females and males:\n')
print (baby_names['Gender'].value_counts())

# grouping the the data by names. This will keep only unique names
names = baby_names.groupby("Name").sum()

# printing the first 5 observations
del names["Year"] # deleting the column "Year"
print ('\nthe first five names in the only-unique-names dataset are:\n', names.head(5))

# sorting it from the biggest value to the smallest one
sorted_names = names.sort_values("Count", ascending = 0)
print ('\nthe top five names in the only-unique-names dataset are:\n', sorted_names.head())

# printing the number of names. Please note that as we have already grouped by the name, 
#	 all the names are unique already
print ('\nthe total number of unique names is', len(names))

# printing the name with the highest occurrence
print ('\nthe name with the highest occurrence is', names.Count.idxmax())

# printing some statistics on the dataset
print ('\nstandard deviation:', names.Count.std())
print ('\ndescriptive statistics:\n', names.describe())
