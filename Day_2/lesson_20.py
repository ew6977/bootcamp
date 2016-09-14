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

    return diameter



a= np.array([[6.7, 1.3, 0.6, 0.7],
            [0.1, 5.5, 0.4, 2.4],
            [1.1, 0.8, 4.5, 1.7],
            [0.0, 1.5, 3.4, 7.5]])

b= np.array([1.1, 2.3, 3.3, 3.9])

#Print row 1 of a
a[1,:]

#Print column 1 and 3 of A
a[:,[1,3]]

#Print the values of every entry in A that is >2
a[a>2]

#ax=b
