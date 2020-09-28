import numpy as np
import numpy.linalg as la

# function that generates the inputs for the students
# Given a list of names for sequences (animals in our case),
# it generates DNA sequences for each and an unknown sequence that we want to classify

def generate_genomic_sequences(names_of_sequences, len_of_strands = 16):
    # create 6 unique 16 base strands
    strand1 = 'ATCGATTGAGCTCTAG'
    strand2 = 'CTAGATTGATCGAGCT'
    strand3 = 'TTCGTAAGCAATGTAA'
    strand4 = 'CCAGCTAGGAACGCAA'
    strand5 = 'CTCGCATGCGCTCTCG'
    strand6 = 'ATCTAGTTATCTCTAT'

    # put all these unique strands in an array
    strands = [strand1, strand2, strand3, strand4, strand5, strand6]

    # select one as our strand that we want to identify
    unknown_strand = np.random.choice(strands)

    # remove the chosen unknown strand from the list of starter strands
    strands.remove(unknown_strand)

    # from the given names of genomes, select one to contain the unknown strand
    idx_of_unknown = np.random.choice(len(names_of_sequences))

    # generate longer strands for each of the names of genomes
    dna_sequences = {}
    for name in names_of_sequences:
        seq = np.random.choice(strands, size = len_of_strands)
        dna_sequences[name] = ''.join(seq)

   
    length_of_strand = len(dna_sequences[names_of_sequences[idx_of_unknown]])
    length_of_unknown = len(unknown_strand)
    idx_of_insert = np.random.choice(int(length_of_strand/length_of_unknown))
    
     # insert the unknown strand into the chosen longer strands at a random place
    seq = dna_sequences[names_of_sequences[idx_of_unknown]]
    seq = seq[0:idx_of_insert*length_of_unknown] + unknown_strand + seq[length_of_unknown*(idx_of_insert+1):]
    dna_sequences[names_of_sequences[idx_of_unknown]] = seq

    return dna_sequences, unknown_strand