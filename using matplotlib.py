# Author: ---
# Date: ---
# EM624 Ex5

# This code will read the data file, count the number of boys, girls, women, and men
# and then create a bar chart. 

import matplotlib.pyplot as plt

# Define the function that will take a line of the file (already split into a list)
# and return a number to indicate the age and gender of the person
def get_index(parts):
	if parts[1] == '1': #male
		if parts[3] == '1': #14-17
			return 0
		else: #>17
			return 2
	else: #female
		if parts[3] == '1': #14-17
			return 1
		else: #>17
			return 3


datafile = open("marketingdata.txt","r")

counts = [0,0,0,0] # list to count number of each type of person

#Go through each row in the data file
for row in datafile:
	if "NA" in row:
		pass #if there's an 'NA' in the row, skip this row
	else:
		parts = row.strip().split() # turn the row into a list
		index = get_index(parts) # find which type of person it is
		counts[index] +=1 # add 1 to the appropriate element in the list

#printing the numerical values
print ("There are", counts[0], "boys")
print ("There are %s men" % counts[2])
print ("There are %s girls" % counts[1])
print ("There are", counts[3], "women")

#creating now the graphs

#first subplot: bar chart
names = ['boys','girls','men','women'] #labels will be used for both the graphs
plt.subplot(221) #defining the position of the graph in the grid [tall, wide, plot#]
x_axis = [1,2,3,4] #set values for the x-axis
plt.bar(x_axis, counts, align='center') #create the bar chart
plt.xticks(x_axis, names) #assign labes to the x-axis

#second subplot: pie chart
plt.subplot(222)
plt.pie(counts,labels=names)

plt.show() #show the bar chart
