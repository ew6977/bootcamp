#Lesson 36 Nonlinear regression

import numpy as np
import pandas as pd
import scipy.optimize
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

df = pd.read_csv('../data/bcd_gradient.csv', comment='#')

df= df.rename(columns={'fractional distance from anterior': 'x',
                       '[bcd] (a.u.)': 'I_bcd'})

plt.plot(df['x'], df['I_bcd'], marker='.', linestyle='none')


#Minimize the square of the distances of the linear regression line

def gradient_model(x, I_0, a, lam):
    """
    Model for bicoid gradient which is exponential decay+ background
    """
    if np.any(np.array(x) < 0):
        raise RuntimeError('x must be positive')
    if np.any(np.array([I_0, a, lam]) < 0):
        raise RuntimeError('all params must be positive')
    return a + I_0 * np.exp(-x / lam)

#Trick to finding decay length of exponential curve:
#decay length is about 1/3 of start

a_guess = 0.2
I_0_guess = 0.9 - 0.2
lam_guess = 0.25

p0 = np.array([I_0_guess, a_guess, lam_guess])

popt, _ = scipy.optimize.curve_fit(gradient_model, df['x'], df['I_bcd'], p0=p0)

x_smooth = np.linspace (0, 1, 200)
I_smooth = gradient_model(x_smooth, *tuple(popt))
plt.plot(x_smooth, I_smooth, color='gray')
plt.show()
