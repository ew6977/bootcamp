#Exersize 1 Using string methods

#a) Write function using for loop, but not built in reversed() function
#material='DNA' is a keyword argument.
def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base. """
    if base in 'Aa':
        if material=='DNA':
            return 'T'
        elif material =='RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid Material')
    elif base in 'TtUu':
        return 'A'
    elif base in "Gg":
        return 'C'
    else:
        return 'G'


def reverse_complement(seq, material='DNA'):
    """ Compute reverse complement of a nucleic acid seq"""
    #Initialize an empty string
    rev_comp = []
    #loop through and add rev comp bases
    for base in seq:
        comp_base=complement_base(base, material=material)
        rev_comp.insert(0, comp_base)
    return ''.join(rev_comp)

# b) Write the function once more without using any loops
def reverse_complement_hard(seq, material='DNA'):
    """This allows you to compute the complement of a nucleic acid seq without
    using any loops"""
    if material=='DNA':
        seq=seq.upper()
        seq_replace_GtoC=seq.replace('G', 'c')
        seq_replace_CtoG=seq_replace_GtoC.replace('C','g')
        seq_replace_TtoA=seq_replace_CtoG.replace('T','a')
        seq_replace_AtoT=seq_replace_TtoA.replace('A','t')
        rev_seq= seq_replace_AtoT[::-1]
    else:
        seq=seq.upper()
        seq_replace_GtoC=seq.replace('G', 'c')
        seq_replace_CtoG=seq_replace_GtoC.replace('C','g')
        seq_replace_TtoA=seq_replace_CtoG.replace('T','a')
        seq_replace_AtoT=seq_replace_TtoA.replace('A','u')
        rev_seq= seq_replace_AtoT[::-1]
    return rev_seq

    ###################################
    #1.4 Longest common substring

def longest_common_substr(seq1, seq2):
    """This function allows you to determine the longest common substring
    that two sequences share."""
    if len(seq1)>len(seq2):
        short_seq_len=len(seq2)
        short_seq=seq2
        long_seq=seq1
    elif len(seq2)>len(seq1):
        short_seq_len=len(seq1)
        short_seq=seq1
        long_seq=seq2
    else:
        shortest=len(seq1)
        short_seq=seq1
        long_seq=seq2
## i=how long seq is, and j=position that seq starts
    for i in range(short_seq_len):
        num_common_check=i+1
        for j in range(short_seq_len-i):
            if short_seq[j:j+num_common_check] in long_seq:
                commonseq= short_seq[j:j+num_common_check]
    return commonseq

#############################
#1.5 RNA secondary structure validator

## make sure that number of closed parenthesis is equal to closed
