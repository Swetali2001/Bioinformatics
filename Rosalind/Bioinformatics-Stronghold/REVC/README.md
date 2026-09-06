# Complementing a Strand of DNA

**Rosalind Problem ID:** REVC

**Track:** Bioinformatics Stronghold

**Language:** Python

## Problem

Given a DNA string, generate its reverse complement.

The complement of each nucleotide is defined as:

- A → T
- T → A
- C → G
- G → C

The reverse complement is obtained by first replacing each nucleotide
with its complementary base and then reversing the resulting sequence.

## Approach

A dictionary is used as a lookup table to map each nucleotide
to its complementary base.

The DNA sequence is traversed using a list comprehension.
The complementary sequence is constructed, and the resulting
sequence is reversed using Python slicing.

## Algorithm

1. Read the DNA sequence from the input file.
2. Create a nucleotide complement lookup table.
3. Replace every nucleotide with its complementary base.
4. Reverse the complemented sequence.
5. Write the resulting reverse complement to the output file.

## Complexity

- Time complexity: O(n)
- Space complexity: O(n)

## Result

The implementation was verified using the official Rosalind
sample dataset.

### Sample Input

```text
AAAACCCGGT
```

### Sample Output

```text
ACCGGGTTTT
```

## Skills Demonstrated

- DNA sequence manipulation
- Nucleotide complementarity
- Python dictionaries
- List comprehensions
- String manipulation
- String slicing
- File input/output
- Functions
- Basic algorithm design
- Computational complexity

## Documentation

A detailed technical report describing the problem, algorithm,
Python implementation, complexity analysis, and verification
is available below.

[Read the Technical Solution Report](Report_Complementing_a_Strand_of_DNA.pdf)
