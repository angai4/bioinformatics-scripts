#!/usr/bin/env python3 

def dna2rna(dna_sequence):
    """
    This function takes a DNA string corresponding to a coding strand and returns the RNA string
    """
    # Convert DNA to RNA by replacing T with U
    rna_sequence = dna_sequence.upper().replace('T', 'U')
    return rna_sequence

def counter(sequence):
    """
    This function takes in a DNA sequence and returns the occurences of each nucleotide 
    """
    # Convert to uppercase to handle both cases
    sequence = sequence.upper()

    # Initialise counters
    A = 0 
    C = 0 
    G = 0
    T = 0

    # Count each nucleotide in sequence
    for nt in sequence:
        if nt == 'A':
            A+=1
        elif nt == 'C':
            C+=1
        elif nt == 'G':
            G+=1
        elif nt == 'T':
            T+=1
    
    return A, C, G, T

def revcomp(sequence):
    """
    This function takes in a DNA sequence and returns its reverse complement
    """
    # Define complement mapping
    comp = {'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'}
    
    # Convert to uppercase for consistency
    sequence = sequence.upper()
    
    # Create reverse complement
    revcomp_seq = ""
    for nt in reversed(sequence):
        revcomp_seq += comp[nt]
    
    return revcomp_seq

def proteinTranslation(seq):
    """ This function translates a nucleic acid sequence into a protein sequnce,
    until the end or until it comes across a stop codon"""
    
    genetic_code = {
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',    # Serine
        'UUC': 'F', 'UUU': 'F',    # Phenylalanine
        'UUA': 'L', 'UUG': 'L',    # Leucine
        'UAC': 'Y', 'UAU': 'Y',    # Tyrosine
        'UAA': None, 'UAG': None,    # Stop
        'UGC': 'C', 'UGU': 'C',    # Cysteine
        'UGA': None,    # Stop
        'UGG': 'W',    # Tryptophan
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',    # Leucine
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',    # Proline
        'CAC': 'H', 'CAU': 'H',    # Histidine
        'CAA': 'Q', 'CAG': 'Q',    # Glutamine
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',    # Arginine
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I',    # Isoleucine
        'AUG': 'M',    # Methionine (Start)
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',    # Threonine
        'AAC': 'N', 'AAU': 'N',    # Asparagine
        'AAA': 'K', 'AAG': 'K',    # Lysine
        'AGC': 'S', 'AGU': 'S',    # Serine
        'AGA': 'R', 'AGG': 'R',    # Arginine
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',    # Valine
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',    # Alanine
        'GAC': 'D', 'GAU': 'D',    # Aspartic Acid
        'GAA': 'E', 'GAG': 'E',    # Glutamic Acid
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G'     # Glycine
        }

    seq = seq.upper().replace('T', 'U')
    proteinSeq = ''

    i = 0 
    while i+2 < len(seq):
        codon = seq[i:i+3]
        aminoAcid = genetic_code[codon]
        
        if aminoAcid is None: # Found stop codon
            break

        proteinSeq = proteinSeq + aminoAcid
        i += 3
    
    return proteinSeq