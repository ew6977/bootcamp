"""
Convert DNA sequences to RNA
For a module, instead of running a function, you just import the module

"""


def rna(seq):
    """
    Convert a DNA sequence to RNA
    """
    #convert to uppercase
    seq=seq.upper()

    return seq.replace('T','U')
