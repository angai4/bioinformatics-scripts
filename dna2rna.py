#!/usr/bin/env python3 

def dna2rna(dna_sequence):
    """
    This function takes a DNA string corresponding to a coding strand and returns the RNA string
    """
    # Convert DNA to RNA by replacing T with U
    rna_sequence = dna_sequence.upper().replace('T', 'U')
    return rna_sequence

def main():
    """Main function to run the DNA to RNA converter"""
    print("DNA to RNA Converter")
    print("-" * 30)
    
    # Get input from user
    dna_sequence = input("Enter a DNA sequence: ").strip()
    
    # Validate input (basic check for valid nucleotides)
    valid_nucleotides = set('ATCG')
    if not all(nt.upper() in valid_nucleotides for nt in dna_sequence):
        print("Error: Please enter a valid DNA sequence containing only A, T, C, G")
        return
    
    # Convert DNA to RNA
    rna_sequence = dna2rna(dna_sequence)
    
    # Display results
    print(f"\nDNA sequence: {dna_sequence.upper()}")
    print(f"RNA sequence: {rna_sequence}")

if __name__ == "__main__":
    main()