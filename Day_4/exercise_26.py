import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Draw a random number
np.random.random()

#The numbers can't be truly random.
#The numbers we pull are psuedo random

#There is a random number generator that
#follows the same sequence every time based on having the same start (seed)
np.random.seed(42)
np.random.random()

#To check that numbers are truly random, plot ECDF
x=np.random.random(size=100000)
#I can't access now, but you would run x through ECDF fxn in na-utils

#Random coin toss
