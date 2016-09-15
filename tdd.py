import pytest
import bioinfo_dicts

def n_neg(seq):
    """
    Number of negative residues in a protien sequence.

    """
    #Convert to uppercase
    seq=seq.upper()

    #Check for validity of sequence
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid')

    #Count Es and Ds and return count
    return seq.count('D') + seq.count('E')
