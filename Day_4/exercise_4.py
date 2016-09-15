import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils as bc_ut
import pandas as pd
import seaborn as sns
sns.set()

#####Exercise 4.1 Long-term trends in hybridization of Darwin Finches#####

#a)Load each file into separate panda DataFrames
df_1973 = pd.read_csv('../data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('../data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('../data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('../data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('../data/grant_2012.csv', comment='#')

#b.1) Chage yearband column name to year in 1973
df_1973 = df_1973.rename(columns={'yearband': 'year'})
df_1973.loc[:, 'year']= '1973'

#b.2) Add year column to other four DataFrames
df_1975.insert(2, 'year', '1975')
df_1987.insert(2, 'year', '1987')
df_1991.insert(2, 'year', '1991')
df_2012.insert(2, 'year', '2012')

#b.3) Change column names so that DataFrames all have the same names

df_1973 = df_1973.rename(columns={'beak length': 'beak length (mm)' ,'beak depth': 'beak depth (mm)'})
df_1975 = df_1975.rename(columns={'Beak length, mm': 'beak length (mm)', 'Beak depth, mm': 'beak depth (mm)'})
df_1987 = df_1987.rename(columns={'Beak length, mm': 'beak length (mm)' ,'Beak depth, mm': 'beak depth (mm)'})
df_1991 = df_1991.rename(columns={'blength': 'beak length (mm)', 'bdepth': 'beak depth (mm)'})
df_2012 = df_2012.rename(columns={'blength': 'beak length (mm)', 'bdepth': 'beak depth (mm)'})

#c) Get rid of duplicate bird measurements

pd.DataFrame.drop_duplicates(df_1973, subset='band', keep= 'first')
pd.DataFrame.drop_duplicates(df_1975, subset='band', keep= 'first')
pd.DataFrame.drop_duplicates(df_1987, subset='band', keep= 'first')
pd.DataFrame.drop_duplicates(df_1991, subset='band', keep= 'first')
pd.DataFrame.drop_duplicates(df_2012, subset='band', keep= 'first')

#b.4) Concatenate Dataframes into a single DataFrame
df_all_beak_data = pd.concat((df_1973, df_1975, df_1987, df_1991, df_2012), ignore_index=True, axis=0)

#c) Save tidy DataFrame in a csv
# all_beak_data.to_csv('all_grant_data', index=False)

#d) Plot an ECDF of beak depths of Geospiza fortis measured in 1987
#f or s for species name
f_1987_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '1987'), 'beak depth (mm)']
f_1987_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '1987'), 'beak length (mm)']

s_1987_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '1987'), 'beak depth (mm)']
s_1987_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '1987'), 'beak length (mm)']

#Calculate the ECDF
f_87d_x, f_87d_y= bc_ut.ecdf(f_1987_depth)
s_87d_x, s_87d_y= bc_ut.ecdf(s_1987_depth)

#close any previous plots
plt.close()

#d) Plot ECDF of beak depths of Fortis
plt.plot(f_87d_x, f_87d_y, marker='.', markersize=7, linestyle='none', alpha=0.5)
plt.plot(s_87d_x, s_87d_y, marker='.', markersize=7, linestyle='none', alpha=0.5)
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
plt.show()
plt.close()
#e) Plot beak depth vs. beak width

plt.plot(f_1987_depth, f_1987_length, marker='.', color= 'blue', markersize=7, linestyle='none', alpha=0.5)
plt.plot(s_1987_depth, s_1987_length, marker='.', color='red', markersize=7, linestyle='none', alpha=0.5)
plt.xlabel('beak depth (mm)')
plt.ylabel('beak width (mm)')
plt.show()

#f) do part e again for all years
#1973
f_1973_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '1973'), 'beak depth (mm)']
f_1973_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '1973'), 'beak length (mm)']
s_1973_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '1973'), 'beak depth (mm)']
s_1973_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '1973'), 'beak length (mm)']

plt.plot(f_1973_depth, f_1973_length, marker='.', color= 'blue', markersize=7, linestyle='none', alpha=0.5)
plt.plot(s_1973_depth, s_1973_length, marker='.', color='red', markersize=7, linestyle='none', alpha=0.5)
plt.xlabel('beak depth (mm)')
plt.ylabel('beak width (mm)')
plt.show()
#1975
f_1975_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '1975'), 'beak depth (mm)']
f_1975_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '1975'), 'beak length (mm)']
s_1975_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '1975'), 'beak depth (mm)']
s_1975_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '1975'), 'beak length (mm)']

plt.plot(f_1975_depth, f_1975_length, marker='.', color= 'blue', markersize=7, linestyle='none', alpha=0.5)
plt.plot(s_1975_depth, s_1975_length, marker='.', color='red', markersize=7, linestyle='none', alpha=0.5)
plt.xlabel('beak depth (mm)')
plt.ylabel('beak width (mm)')
plt.show()

#1991
f_1991_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '1991'), 'beak depth (mm)']
f_1991_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '1991'), 'beak length (mm)']
s_1991_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '1991'), 'beak depth (mm)']
s_1991_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '1991'), 'beak length (mm)']

plt.plot(f_1991_depth, f_1991_length, marker='.', color= 'blue', markersize=7, linestyle='none', alpha=0.5)
plt.plot(s_1991_depth, s_1991_length, marker='.', color='red', markersize=7, linestyle='none', alpha=0.5)
plt.xlabel('beak depth (mm)')
plt.ylabel('beak width (mm)')
plt.show()

#2012
f_2012_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '2012'), 'beak depth (mm)']
f_2012_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'fortis') & (df_all_beak_data['year'] == '2012'), 'beak length (mm)']
s_2012_depth = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '2012'), 'beak depth (mm)']
s_2012_length = df_all_beak_data.loc[(df_all_beak_data['species'] == 'scandens') & (df_all_beak_data['year'] == '2012'), 'beak length (mm)']

plt.plot(f_2012_depth, f_2012_length, marker='.', color= 'blue', markersize=7, linestyle='none', alpha=0.5)
plt.plot(s_2012_depth, s_2012_length, marker='.', color='red', markersize=7, linestyle='none', alpha=0.5)
plt.xlabel('beak depth (mm)')
plt.ylabel('beak width (mm)')
plt.show()
