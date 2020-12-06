'''
Author: ---
Date: ---
Solution to EX03

'''

### ---------------------------------------------------------------------------------
# Part 1. Read the Marketing Data file, print the first 6 rows and count how many lines
# are in the file. 

marketing_file = open('marketingdata.txt', 'r')

# Initialize the counter for lines with no 'NA'
row_with_no_NA_counter = 0
row_counter = 0
# Loop through the file
print('\n---These are the first fifteen lines in the file with no "NA" in it:')
for row in marketing_file:
    if 'NA' not in row: # to check that the row has one or more "NA" element  or not
        if row_with_no_NA_counter < 15: # to check we already passed 15 lines with no 'NA' or not
            print('  ', row)
        row_with_no_NA_counter += 1 #equivalent to row_counter = row_counter + 1
    row_counter += 1



print('---There file has {} lines with no "NA" in it out of {} lines'
      .format(row_with_no_NA_counter, row_counter))

### ---------------------------------------------------------------------------------
# Part 2. Read the CitiBike CSV file and count the number of lines and 
# the number of lines with '1/15/2014' in them. Also print the first 5 lines containing 'NA'

# Opening the csv file
citi_file = open('NYC-CitiBike-2016.csv', 'r')

# Initialize the 2 counters we'll need
line_counter = 0
date_counter = 0

# Loop through the lines in the file
for text_line in citi_file:
    
    if '9/29/16' in text_line:
        #print('\n---this line is for September 29th 2016')
        #\n is equivalent to print a blank line
        #print('  ', text_line)
        date_counter += 1 #shorthand for adding 1 to the date_counter, this is equivalent to date_counter = date_counter + 1
        
    line_counter += 1 #equivalent to line_counter = line_counter + 1

print('\n---There are', line_counter, 'lines in the file, of which', date_counter, 'from September 29th 2016')

if  row_with_no_NA_counter > date_counter:
    print( 'The first file is larger than the second one')
else:
    print('The first file is smaller than the second one')