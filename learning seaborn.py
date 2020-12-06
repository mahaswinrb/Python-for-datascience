# author: xxxx
# seaborn example 

# import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read file into pandas
rfile = pd.read_csv('Rate_PUF.csv')

# create the data structure for "Month"
rfile.ImportDate = pd.to_datetime(rfile.ImportDate)
rfile['Month'] = rfile.ImportDate.dt.month

# prepare the plotting
sns.set_style('whitegrid')
ax = sns.countplot(x = "Month", data = rfile, color = "lightsteelblue")
ax.set_xlabel('Month', fontsize = 14)
ax.set_ylabel('Number of Registerations', fontsize = 14)
ax.set_title('Insured by the month in New Jersey', fontsize = 18)
ax.tick_params(labelsize = 10)

# plotting
plt.show()
