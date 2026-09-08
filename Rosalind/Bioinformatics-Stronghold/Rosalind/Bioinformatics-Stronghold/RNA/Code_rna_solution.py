"""
Rosalind Problem: Transcribing DNA into RNA
--------------------------------------------
Task:
    Given a DNA string 't' (length at most 1000 nt), produce its
    transcribed RNA string 'u' by replacing every occurrence of
    Thymine ('T') with Uracil ('U'). All other bases (A, C, G)
    stay the same.

Input:
    A plain text file named 'rosalind_rna.txt' containing a single
    line with the DNA string.

Output:
    A plain text file named 'rosalind_rna_output.txt' containing a
    single line with the transcribed RNA string.
"""

# ---------------------------------------------------------------------
# File names used for input and output.
# Keeping them as named constants (instead of "magic strings" scattered
# through the code) makes the script easier to read and update.
# ---------------------------------------------------------------------
INPUT_FILE = "rosalind_rna.txt"
OUTPUT_FILE = "rosalind_rna_output.txt"





# ---------------------------------------------------------------------
# FUNCTIONS USED IN THIS SCRIPT (4 custom functions total):
#   1. transcribe_dna_to_rna(dna_string)   -> does the actual DNA->RNA conversion
#   2. read_dna_sequence(file_path)        -> reads the DNA string from a file
#   3. write_rna_sequence(file_path, rna)  -> writes the RNA string to a file
#   4. main()                              -> runs steps 1-3 in order
#
# Each one is defined with "def" below and marked with a comment
# "# FUNCTION:" right above it, so they're easy to spot.
# ---------------------------------------------------------------------


# FUNCTION: transcribe_dna_to_rna
def transcribe_dna_to_rna(dna_string):
    """
    Transcribe a DNA sequence into an RNA sequence.

    Every 'T' (Thymine) in the DNA string is replaced with
    'U' (Uracil), which is the only difference between DNA and RNA
    at the level of a coding strand.

    Parameters
    ----------
    dna_string : str
        A DNA sequence made up of the letters A, C, G, and T.

    Returns
    -------
    str
        The transcribed RNA sequence, with every 'T' replaced by 'U'.

    Example
    -------
    >>> transcribe_dna_to_rna("GATGGAACTTGACTACGTAAATT")
    'GAUGGAACUUGACUACGUAAAUU'
    """
    return dna_string.replace("T", "U")


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
def write_rna_sequence(file_path, rna_string):
    """
    Write an RNA sequence to a text file, followed by a newline.

    Parameters
    ----------
    file_path : str
        Path to the output file to create (or overwrite).
    rna_string : str
        The RNA sequence to write to the file.
    """
    with open(file_path, "w") as output_file:
        output_file.write(rna_string + "\n")


# FUNCTION: main
def main():
    """
    Run the full workflow:
    1. Read the DNA sequence from INPUT_FILE.
    2. Transcribe it into RNA.
    3. Write the RNA sequence to OUTPUT_FILE.
    4. Print the result to the screen as well, for a quick check.
    """
    dna_string = read_dna_sequence(INPUT_FILE)
    rna_string = transcribe_dna_to_rna(dna_string)
    write_rna_sequence(OUTPUT_FILE, rna_string)

    print(f"Transcribed RNA string written to '{OUTPUT_FILE}':")
    print(rna_string)


# The "if __name__ == '__main__':" guard means main() only runs when
# this file is executed directly (e.g. `python rosalind_rna_solution.py`),
# not when it's imported as a module into another script.
if __name__ == "__main__":
    main()