# dna_nucleotide_analyzer.py

"""
DNA Nucleotide Analyzer

Reads a DNA sequence, counts the frequency of A, T, G, and C nucleotides,
and displays a bar chart using matplotlib.

Author: [Your Name]
"""

from collections import Counter
import matplotlib.pyplot as plt


def read_dna_sequence(file_path):
    """Reads a DNA sequence from a file and filters invalid characters."""
    with open(file_path, 'r') as file:
        raw = file.read().replace('\n', '').upper()
        cleaned = ''.join([nt for nt in raw if nt in "ATGC"])
    return cleaned


def count_nucleotides(sequence):
    """Counts A, T, G, C nucleotides in the sequence."""
    return Counter(sequence)


def plot_nucleotide_counts(counts):
    """Plots a bar chart of nucleotide counts."""
    labels = counts.keys()
    values = counts.values()

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=["#ff4d4d", "#4d94ff", "#33cc33", "#ffcc00"])
    plt.title("Nucleotide Frequency")
    plt.xlabel("Nucleotide")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def main():
    file_path = "sample_dna.txt"  # Make sure this file exists
    dna_sequence = read_dna_sequence(file_path)
    counts = count_nucleotides(dna_sequence)

    print("Nucleotide counts:")
    for nt, count in counts.items():
        print(f"  {nt}: {count}")

    plot_nucleotide_counts(counts)


if __name__ == "__main__":
    main()
