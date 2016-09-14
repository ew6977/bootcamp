#Anatomy of a function:
#Define a function called ratio.
#def defines a function. next comes the name of the function. This is called the call signature
#The colon says that the new level of indentation is part of the function
#"""Triple quoted string is the "Docstring" which should tell you what the code does"""
#Return statement is the output of the function

#Example of a function
def ratio(x,y):
    """The ratio of X to Y"""
    return x/y

#Example of a function that does not need an argument
def answer_to_the_ultimate_question_of_life_and_the_universe():
    """Simpler program that Deep Thought's, I bet."""
    return 42

#A function need not return anything.
def think_too_much():
    """Express Ceasar's skepticism about Cassius."""
    print ("""Yond Cassius has a lean and hungry look,
    He thinks too much; such men are dangerous""")

#A more useful function example. This is also a nice example of modular programming
#Modular programming allows you to break functions up and call each other.

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
    rev_comp = ''
    #loop through and add rev comp bases
    for base in reversed(seq):
        rev_comp+= complement_base(base, material=material)
    return rev_comp
