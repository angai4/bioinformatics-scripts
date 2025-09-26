#!/usr/bin/env python 

# This function takes in a DNA sequence and returns its reverse complement
def revc(sequence):
    
    comp = {'A':'T', 
        'C':'G', 
        'G':'C', 
        'T':'A'}
    revcomp = ''
    revseq = ''.join(reversed(sequence))
    for nt in revseq:
        revcomp = revcomp + comp[nt]
    print(revcomp)
