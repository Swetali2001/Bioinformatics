"""
Rosalind Problem: Complementing a Strand of DNA
------------------------------------------------
Task:
    Given a DNA string 's' (length at most 1000 bp), produce its
    reverse complement 's^c'. The reverse complement is formed by:
        1. Replacing each base with its complement
           (A <-> T, C <-> G).
        2. Reversing the resulting string.

Input:
    A plain text file named 'rosalind_revc.txt' containing a single
    line with the DNA string.

Output:
    A plain text file named 'rosalind_revc_output.txt' containing a
    single line with the reverse complement string.
"""

# ---------------------------------------------------------------------
# File names used for input and output.
# Keeping them as named constants (instead of "magic strings" scattered
# through the code) makes the script easier to read and update.
# ---------------------------------------------------------------------
INPUT_FILE = "rosalind_revc.txt"
OUTPUT_FILE = "rosalind_revc_output.txt"

# ---------------------------------------------------------------------
# Lookup table for complementary DNA bases.
# A pairs with T, and C pairs with G (Watson-Crick base pairing).
# ---------------------------------------------------------------------
COMPLEMENT = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
}

# ---------------------------------------------------------------------
# FUNCTIONS USED IN THIS SCRIPT (4 custom functions total):
#   1. reverse_complement(dna_string)      -> computes the reverse complement
#   2. read_dna_sequence(file_path)        -> reads the DNA string from a file
#   3. write_rna_sequence(file_path, seq)  -> writes the result to a file
#   4. main()                              -> runs steps 1-3 in order
#
# Each one is defined with "def" below and marked with a comment
# "# FUNCTION:" right above it, so they're easy to spot.
# ---------------------------------------------------------------------


# FUNCTION: reverse_complement
def reverse_complement(dna_string):
    """
    Compute the reverse complement of a DNA sequence.

    Every base is first replaced by its complementary base
    (A <-> T, C <-> G) using the COMPLEMENT lookup table, and the
    resulting complemented string is then reversed.

    Parameters
    ----------
    dna_string : str
        A DNA sequence made up of the letters A, C, G, and T.

    Returns
    -------
    str
        The reverse complement of the input DNA sequence.

    Example
    -------
    >>> reverse_complement("AAAACCCGGT")
    'ACCGGGTTTT'
    """
    # Step 1: replace each base with its complement.
    complemented_bases = [COMPLEMENT[base] for base in dna_string]
    complement_string = "".join(complemented_bases)

    # Step 2: reverse the complemented string.
    return complement_string[::-1]


# FUNCTION: read_dna_sequence
def read_dna_sequence(file_path):
    """
    Read a DNA sequence from a text file.

    The file is expected to contain a single line with the DNA
    string. Leading/trailing whitespace (including the newline at
    the end of the file) is removed.

    Parameters
    ----------
    file_path : str
        Path to the input file containing the DNA sequence.

    Returns
    -------
    str
        The DNA sequence as a clean string (no surrounding whitespace).
    """
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


# FUNCTION: write_rna_sequence
def write_rna_sequence(file_path, sequence):
    """
    Write a sequence to a text file, followed by a newline.

    Parameters
    ----------
    file_path : str
        Path to the output file to create (or overwrite).
    sequence : str
        The sequence to write to the file.
    """
    with open(file_path, "w") as output_file:
        output_file.write(sequence + "\n")


# FUNCTION: main
def main():
    """
    Run the full workflow:
    1. Read the DNA sequence from INPUT_FILE.
    2. Compute its reverse complement.
    3. Write the reverse complement to OUTPUT_FILE.
    4. Print the result to the screen as well, for a quick check.
    """
    dna_string = read_dna_sequence(INPUT_FILE)
    result = reverse_complement(dna_string)
    write_rna_sequence(OUTPUT_FILE, result)

    print(f"Reverse complement written to '{OUTPUT_FILE}':")
    print(result)


# The "if __name__ == '__main__':" guard means main() only runs when
# this file is executed directly (e.g. `python rosalind_revc_solution.py`),
# not when it's imported as a module into another script.
if __name__ == "__main__":
    main()
