import numpy as np

xa_high= np.loadtxt('data/xa_high_food.csv', comments= '#')
xa_low= np.loadtxt('data/xa_low_food.csv', comments= '#')

def xa_to_diameter(xa):
    """
    Covert an array of cross sectional areas to diameters with commensurate units
    """

    #Compute the diameter from area
    #Area= pi *d^2/4
    diameter= np.sqrt(xa *4 /np.pi)
