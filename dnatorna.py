"""
convert DNA to RNA
"""

def rna(seq):
    """ convert DNA tO RNA"""
    # determibe if the original seq was uppercase
    seq_upper=seq.isupper()
    #convert to lower case

    seq=seq.lower()

    # swap out t for u
    seq=seq.replace('t','u')

    # return upper or lower depends on input
    if seq_upper:
        return seq.upper()
    else:
        return seq


def reverse_rna_complement(seq):
    """ convert dna to reversed complement rna"""

    # Determine if original was uppercase
    seq_upper = seq.isupper()

    # Reverse sequence
    seq = seq[::-1]

    # Convert to upper
    seq = seq.upper()

    # Compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    # Return result
    if seq_upper:
        return seq.upper()
    else:
        return seq
