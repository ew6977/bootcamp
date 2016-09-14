import numpy as np
import scipy.stats

import matplotlib.pyplot as plt

import seaborn as sns
rc={'lines.linewidth':2, 'axes.labelsize': 18, 'axes.titlesize':18}
sns.set(rc=rc)

def ecdf(data):
    """
    Compute x, y values for an empirical distribution

    """
    #data is a vector of values
    x =np.sort(data)
    y= np.arange(1, 1+len(x)) / len(x)

    return x,y


#load data
xa_high =np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low =np.loadtxt('data/xa_low_food.csv', comments='#')

plt.close()
x_high, y_high= ecdf(xa_high)
x_low, y_low = ecdf(xa_low)
plt.plot(x_high, y_high, markersize=20, marker='.', linestyle='none', alpha=0.5)
plt.plot(x_low, y_low, markersize=20, marker='.', linestyle='none', alpha=0.5)
plt.xlabel('Cross secional area (um)')
plt.ylabel('eCDF')
plt.legend(('high concentration', 'low concentration',), loc= 'lower right' )
plt.show()
