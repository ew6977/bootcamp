import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils as bc_ut
import pandas as pd
import seaborn as sns
sns.set()

df = pd.read_csv('../data/frog_tongue_adhesion.csv', comment='#')

df=df.rename(columns={'impact force (mN)':'impf'})

gb_frog= df.groupby('ID')

#Do operations on grouby
mean_impf= gb_frog['impf'].mean()
sem_impf = gb_frog['impf'].sem()

# #YOU DON'T NEED groupby now becasue of seaborn
# sns.barplot(data=df, x='ID', y='impf')
# plt.show()
# plt.close()
# #Justin says "Lets actually plot all of our data"
# sns.swarmplot(data=df, x='ID', y='impf')
# plt.show()
# plt.close()

# #You can also color the data points out by date
# sns.swarmplot(data=df, x='ID', y='impf', hue='date')
# plt.gca().legend_.remove()
# plt.show()
# 
# #do a boxplot
# sns.boxplot(data=df, x='ID', y='impf')
# plt.show()
