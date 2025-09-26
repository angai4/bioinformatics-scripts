#!/usr/bin/env python3 

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

def main():
    """Main function to run the reverse complement generator"""
    print("DNA Reverse Complement Generator")
    print("-" * 40)
    
    # Get input from user
    dna_sequence = input("Enter a DNA sequence: ").strip()
    
    # Validate input (basic check for valid nucleotides)
    valid_nucleotides = set('ATCG')
    if not all(nt.upper() in valid_nucleotides for nt in dna_sequence):
        print("Error: Please enter a valid DNA sequence containing only A, T, C, G")
        return
    
    # Generate reverse complement
    reverse_complement = revcomp(dna_sequence)
    
    # Display results
    print(f"\nOriginal sequence:    5'-{dna_sequence.upper()}-3'")
    print(f"Reverse complement:   3'-{reverse_complement}-5'")

if __name__ == "__main__":
    main()
