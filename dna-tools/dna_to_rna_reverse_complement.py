from Bio.Seq import Seq

# Define a DNA sequence
dna_sequence = Seq("ATGCGTACGTTAG")

# Transcribe DNA to RNA (T -> U)
rna_sequence = dna_sequence.transcribe()

# Get the reverse complement of the DNA
reverse_complement = dna_sequence.reverse_complement()

# Print results
print("Original DNA Sequence:        ", dna_sequence)
print("Transcribed RNA Sequence:     ", rna_sequence)
print("Reverse Complement of DNA:    ", reverse_complement)
