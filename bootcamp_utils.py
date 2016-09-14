"""
bootcamp_utils: A collection of statistical functions
# proved useful 55 students
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def ecdf(data):
    """
    Compute x, y values for an empirical distribution function.
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)
    return x, y

def draw_bs_reps(data, func, size=1):
    """
    draw_bs_reps(data, func, size)

    This function takes an array and returns a statistic.
    Examples that could be passed in as 'func' are:
        - np.mean
        - np.std
        - np.median
        - User defined function
    'Size' is the number of replicates to generate
    """
    n_reps= size
    bs_replicates= np.empty(n_reps)
    for i in range(n_reps):
            bs_sample= np.random.choice(data, replace=True, size=len(data))
            bs_replicates[i]=func(bs_sample)
    return bs_replicates


def confinterval95(data, func, size=1):
    """
    confidenceinterval95(data, func, size)

    This function takes an array and returns a 95 percent confidence interval.
    Examples that could be passed in as 'func' are:
        - np.mean
        - np.std
        - np.median
        - User defined function
    'Size' is the number of replicates to generate
    """
    n_reps= size
    bs_replicates= np.empty(n_reps)
    for i in range(n_reps):
            bs_sample= np.random.choice(data, replace=True, size=len(data))
            bs_replicates[i]=func(bs_sample)
    conf_int= np.percentile(bs_replicates, [2.5, 97.5])
    return conf_int
