import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Specify parameters
#Number of generations
n_gen=16 #generations

#Chance of having a beneficial mutation
r=1e-5

#Total number of cells
n_cells = 2**(n_gen-1)

#adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

#report mean and std
print('AI mean:', np.mean(ai_samples))
print('AI std:', np.std(ai_samples))
#Fano factor is ratio of variance to the mean
print('AI Fano:', np.var(ai_samples) / np.mean(ai_samples))

#Function to draw out of a random mutation hypothesis

def draw_random_mutation(n_gen, r):
    """
    Draw sample under random mutation hypothesis
    """
    #Initialize number of mutations
    n_mut=0
    for g in range(n_gen):
        #This doesn't take into consideration mutations can occur that make cell lose immunity
        n_mut = 2*n_mut + np.random.binomial(2**g-2*n_mut, r)
    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    #Initialize
    samples= np.empty(size)

    #Draw the samples
    for i in range(size):
        samples[i]=draw_random_mutation(n_gen, r)

    return samples


rm_samples=sample_random_mutation(n_gen, r, size=100000)
print('RM mean:', np.mean(rm_samples))
print('RM std:', np.std(rm_samples))
#Fano factor is ratio of variance to the mean
print('RM Fano:', np.var(rm_samples) / np.mean(rm_samples))
