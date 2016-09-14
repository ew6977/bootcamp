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

plt.semilogx(wt_iptg_conc, wt_iptg_fc, markersize=20, marker='.', linestyle='none', alpha=0.5)
plt.semilogx(q18m_iptg_conc, q18m_iptg_fc, markersize=20, marker='.', linestyle='none', alpha=0.5)
plt.semilogx(q18a_iptg_conc, q18a_iptg_fc, markersize=20, marker='.', linestyle='none', alpha=0.5)
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold change')
plt.title('IPTG conc (mM) vs. Fold Change')


#c) Write function to compute the theoretical fold change

def foldchange(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    numerator= RK * (1 + c / KdA)**2
    denomenator= (1 + c / KdA)**2 + Kswitch*(1 + c / KdI)**2
    fc= (1 + numerator / denomenator)**-1
    return fc

#d) Plot a smooth curve showing theoretical fold change

#find min and max of iptg concs of 3 diff mutants
all_conc= (wt_iptg_conc, q18m_iptg_conc, q18a_iptg_conc)
conc_concat=np.concatenate(all_conc)
conc_min=np.min(conc_concat)
conc_max=np.max(conc_concat)
log_conc_min= np.log10(conc_min)
log_conc_max= np.log10(conc_max)

iptg_theo_conc=np.logspace(log_conc_min, log_conc_max, num=100)

plt.semilogx(iptg_theo_conc, foldchange(iptg_theo_conc, 141.5), linewidth=2)
plt.semilogx(iptg_theo_conc, foldchange(iptg_theo_conc, 16.56), linewidth=2)
plt.semilogx(iptg_theo_conc, foldchange(iptg_theo_conc, 1332), linewidth=2)

# plt.show()
plt.close()

#e)
#1)Write a function bohr_parameter
def bohr_parameter(c, RK,KdA=0.017, KdI=0.002, Kswitch=5.8):
    lnRK= np.log(RK)
    numerator= (1 + c / KdA)**2
    denomenator= (1 + c / KdA)**2 + Kswitch*(1 + c / KdI)**2
    bohr_parameter= -lnRK- np.log(1 + numerator / denomenator)
    return bohr_parameter
#2 write fold change bohr function
def fold_change_bohr(bohr_parameter):
    fc= 1 / (1 + np.exp(-bohr_parameter))
    return fc
#3 generate values of bohr parameter ranging from -6 to 6
negsixtosix= np.arange(-6,6)

#4 Compute theoretical fold change as fxn of bohr_parameter
plt.plot(negsixtosix, fold_change_bohr(negsixtosix), linewidth=2)
plt.show()
