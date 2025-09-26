#!/usr/bin/env python3

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

def main():
    """Main function to run the nucleotide counter"""
    print("DNA Nucleotide Counter")
    print("-" * 30)
    
    # Get input from user
    dna_sequence = input("Enter a DNA sequence: ").strip()
    
    # Validate input (basic check for valid nucleotides)
    valid_nucleotides = set('ATCG')
    if not all(nt.upper() in valid_nucleotides for nt in dna_sequence):
        print("Error: Please enter a valid DNA sequence containing only A, T, C, G")
        return
    
    # Count nucleotides
    A, C, G, T = counter(dna_sequence)
    
    # Display results
    print(f"\nResults for sequence: {dna_sequence.upper()}")
    print(f"A: {A}")
    print(f"C: {C}")
    print(f"G: {G}")
    print(f"T: {T}")
    print(f"Total length: {len(dna_sequence)}")

if __name__ == "__main__":
    main()

