#!/usr/bin/env python 

# This function takes in a DNA sequence and returns the occurences of each nucleotide
def counter(sequence):
    A = 0 
    C = 0 
    G = 0
    T = 0
    for nt in sequence:
        if 'A' in nt:
            A+=1
        elif 'C' in nt:
            C+=1
        elif 'G' in nt:
            G+=1
        elif 'T' in nt:
            T+=1
    
    print(A, C, G, T)

