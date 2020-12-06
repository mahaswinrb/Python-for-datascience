"""
Author ----
Date ----

EMx24 Exercise 4:

The idea is that you will have one list ('data') and each
item/element in that list is itself a list. Those sublists 
each correspond to one row from the data file.

Like this: 
list_of_lists = []
then after reading in the file:
list of lists = [[1, 2, 3], 
			  	 [4, 5, 6],  <- one row from file
			  	 [7, 8, 9]]
"""
import csv
import pandas as pd

# Create function to calculate total passes, average miles and print details
def print_details(data_list):
    total_passes = 0
    total_miles = 0
    for day in data_list:
        miles = float(day[3])
        total_miles = total_miles + miles
        passes = float(day[7])
        total_passes = total_passes + passes
    average_miles = total_miles/len(data_list)
    print ('\n-- This data is from', data_list[0][0], 'to', data_list[len(data_list)-1][0],':')
    print ('\n   The average daily miles traveled in this month is', average_miles, 'miles')
    print ('\n   The total 24-Hour passes purchased this month was', total_passes, 'passes')
    
    top_trips = sorted(data_list, key=lambda x:int(x[1]), reverse=True)
    top = []
    top.append([x[0] for x in top_trips])
    print ('\n   The 5 days with more daily trips for this month are:', top[0][:5])
    return

# Open txt and extract list from June
infile_txt = open('citi_bike.txt','r')
data_june = [] # <- our empty list

# Loop through file
for row_txt in infile_txt:
    # "parts" is now the list form of the row
    parts = row_txt.strip().split()
    # checking for data from month 6
    if parts[0].startswith('6'):
    # added this row to the "data_june" lists of lists
        data_june.append(parts)

# Open csv and extract list from January 
infile_csv = open('citi_bike.csv','r')
data_january = [] # <- our empty list
csv_parsed = csv.reader(infile_csv) # Compiling CSV file into lists

# Loop through file
for row_csv in csv_parsed:
    if row_csv[0].startswith('1'): # <- only data from month 1
        data_january.append(row_csv) # <- added this row to the "data_january" lists of lists

# Call function for each file
print_details(data_june)
print_details(data_january)

# Close files
infile_txt.close()
infile_csv.close()

# the following is the pandas portion
print ('\n-- Working now with pandas...')

# creating a list with the header names
#header_names = ['date', 'trips24', 'cum_trips', 'miles_today', 'miles_todate',
#    'tot_annual_members', 'annual_members', '24h_passes', '7d_passes']

#reading ther 2 files into a pandas structure and printing its lenght
txt_portion = pd.read_csv('citi_bike.txt', sep = " ", header = None)
#txt_portion.columns = header_names
print ('\n   The number of rows for the pandas - text portion is:', len(txt_portion.axes[0]))

csv_portion = pd.read_csv('citi_bike.csv', sep = ",", header = None)
#csv_portion.columns = header_names
print ('\n   The number of rows for the pandas - csv portion is:', len(csv_portion.axes[0]))

# using the 'concat' functions to join/append the dataframes into one
merged_data = pd.concat([txt_portion,csv_portion],axis = 0)

# printing the lenght of new dataframe
print ('\n   The size of the the new/merged dataframe is:')
print ('    number of rows:', len(merged_data.axes[0]))
print ('    number of columns:', len(merged_data.axes[1]))


print ('\n--- This is the end of the files processing ---')
