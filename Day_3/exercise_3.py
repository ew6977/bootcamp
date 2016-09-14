import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

########Exercise 3.2 Data collapse############

#a) load in the three data sets

wt_data= np.loadtxt('../data/wt_lac.csv', comments= '#', delimiter=',', skiprows=3)
q18m_data= np.loadtxt('../data/q18m_lac.csv', comments= '#', delimiter=',', skiprows=3)
q18a_data= np.loadtxt('../data/q18a_lac.csv', comments= '#', delimiter=',', skiprows=3)

#b) make a plot of fold change IPTG concentration for each of the three mutants

#Pull out concentrations and fold changes
wt_iptg_conc= wt_data[:,0]
wt_iptg_fc= wt_data[:,1]

q18m_iptg_conc=q18m_data[:,0]
q18m_iptg_fc=q18m_data[:,1]

q18a_iptg_conc=q18a_data[:,0]
q18a_iptg_fc=q18a_data[:,1]

#make sure previous plots have been closed
plt.close()
#plot the data

plt.plot(wt_iptg_conc, wt_iptg_fc, markersize=20, marker='.', linestyle='none', alpha=0.5)
plt.plot(q18m_iptg_conc, q18m_iptg_fc, markersize=20, marker='.', linestyle='none', alpha=0.5)
plt.plot(q18a_iptg_conc, q18a_iptg_fc, markersize=20, marker='.', linestyle='none', alpha=0.5)
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold change')
plt.xscale('log')
plt.title('IPTG conc (mM) vs. Fold Change')
plt.show()

#c) Write function to compute the theoretical fold change

def foldchange(c, RK, KdA=0.017)
