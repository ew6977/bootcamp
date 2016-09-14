import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#set matplotlib rc parameters
rc={'lines.linewidth':2, 'axes.labelsize':18,
    'axes.titlesize': 18}
sns.set(rc=rc)

#load the food data
xa_high =np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low =np.loadtxt('data/xa_low_food.csv', comments='#')

#Make bin boundaries
#What this means is go from 1700 to 2500 and take steps of 50 so we have bins of 50
#Bins are super important. It can change the way the data is displayed.
low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_min = np.min(xa_high)
high_max = np.min(xa_high)
global_min = np.min([low_min, high_min])
global_max = np.max([low_max, high_max])

bins=np.arange(global_min-50, global_max+50, 50)

#Plot data as a histogram
#Focus on low conc first

_ = plt.hist(xa_high, bins=bins)
plt.xlabel('Cross sectional area (µm$^2$)')
plt.ylabel('count')
plt.close()
#Plot data as two overlayed histograms
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
plt.xlabel('Cross sectional area (µm$^2$)')
plt.ylabel('frequency')
plt.legend(('low concentration', 'high concentration'), loc='upper right')


#save the figure
plt.savefig('egg_area_histograms.pdf', bbox_inches='tight')
plt.show()
