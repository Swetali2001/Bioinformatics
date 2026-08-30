"""
Rosalind Problem: Counting DNA Nucleotides (DNA)
--------------------------------------------------
Task:
    Given a DNA string s of length at most 1000 nt, count how many
    times each of the four nucleotide symbols ('A', 'C', 'G', 'T')
    occurs in s.

Input:
    A plain text file named 'rosalind_dna.txt' containing a single
    line with the DNA string.

Output:
    Four space-separated integers giving the counts of 'A', 'C', 'G',
    and 'T', respectively, in that exact order.
"""


def count_nucleotides(dna_string):
    """
    Count the occurrences of each nucleotide (A, C, G, T).

    Parameters
    ----------
    dna_string : str
        A DNA sequence containing A, C, G, and T.

    Returns
    -------
    dict
        Dictionary mapping each nucleotide to its count.
    """

    # Initialize a counter for each of the four nucleotides.
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # Traverse the DNA sequence one nucleotide at a time.
    for nucleotide in dna_string:
        counts[nucleotide] += 1

    return counts


# Read the DNA sequence from the input file.
# .strip() removes leading/trailing whitespace, including newlines.
with open('rosalind_dna.txt') as f:
    dna_sequence = f.read().strip()

# Count the nucleotides.
counts = count_nucleotides(dna_sequence)

# Print the counts in the order required by Rosalind: A, C, G, T.
print(counts['A'], counts['C'], counts['G'], counts['T'])
