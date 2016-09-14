import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

########Exercise 3.2 Data collapse############

#a) load in the three data sets

wt_lac_data= np.loadtxt('~/git/bootcamp/data/wt_lac.csv', comment= '#')
q18m_lac= np.loadtxt('~/git/bootcamp/data/q18m_lac.csv', comment= '#')
q18a_lac= np.loadtxt('~/git/bootcamp/data/q18a_lac.csv', comment= '#')
