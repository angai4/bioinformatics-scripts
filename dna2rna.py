#!/usr/bin/env python 

# This function takes a DNA string corresponding to a coding strand, returns the transcribed RNA string
def dna2rna(dna_sequence):
    replace = dna_sequence.replace('T', 'U')
    print(replace)