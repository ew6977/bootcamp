#Exercise 2
import os
import numpy

###########Exercise 2.2 Parsing a FASTA file###################
#b) Use file  I/O skills learned to read in sequence and store
# it as a single string with no gaps


with open('data/salmonella_spi1_region.fna', 'r') as f, open('salmonella_seq_uninterrupted.txt', 'w') as f_out:
    #Get all of the lines
    lines=f.readlines()
    salmon_cat_seq=[]

    #Put the lines that contain sequence into a string
    for line in lines:
        if '>' not in line:
            f_out.write(line)

###########Exercise 2.3 Pathogenicity islands###################




#def gc_blocks(seq, block_size):
#    if type(block_size) != int or block_size <= 0:
#        RuntimeError('Do not be dumb. Put in an integer.')
#    number_of_blocks= len(seq)//block_size
#    new_seq_len=
#    divided_seq=()

#def gc_content()

###########Exersise 2.4 ORF Detection###################

start_codon='ATG'
stop_codons=['TGA', 'TGA', 'TAA']

def longest_orf(seq):
    start_codon_indices=[]
    stop_codon_indices=[]
    valid_reading_frames=[]

    #Find all start codon indices
    for i, _ in enumerate(seq):
        if seq[i:i+3] == start_codon:
            start_codon_indices += [i]

    #Find all stop codon indices
    for i, _ in enumerate(seq):
        if seq[i:i+3] in stop_codons:
            stop_codon_indices += [i]

    #Determine if start/stop codon pair is in frame
    for i in stop_codon_indices:
        possible_stop = i
        print(possible_stop)
        for i in start_codon_indices:
            possible_start = i
            possible_frame = possible_stop - possible_start
            if possible_frame % 3 == 0:
                aa_len = possible_frame / 3
                valid_reading_frames += [aa_len]
    return valid_reading_frames
