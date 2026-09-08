Transcribing DNA into RNA (RNA)

**Rosalind Problem ID:** RNA
**Link:** https://rosalind.info/problems/rna/

## Problem
An RNA string is formed from a DNA string by replacing all occurrences of thymine (T) with uracil (U). This problem asks for the transcription of a given DNA string into its corresponding RNA string.

**Given:** A DNA string t having length at most 1000 nt.
**Return:** The transcribed RNA string of t.

### Sample Dataset

GATGGAACTTGACTACGTAAATT


### Sample Output

GAUGGAACUUGACUACGUAAAUU


## Approach
• Read the DNA string t from the input file.
• Strip any trailing whitespace/newline characters introduced by file I/O.
• Replace every T character with U.
• Output the resulting RNA string u to a file.
Runs in O(n) time and O(n) space, where n is the length of the DNA string.

## Files
| File | Description |
|---|---|
| `Code_rna_solution.py` | Python solution (function to transcribe DNA to RNA via character replacement) |
| `Report_on_Transcribing_DNA_into_RNA.pdf` | Full write-up: problem overview, approach, algorithm, complexity analysis, and results |
| `rosalind_rna_1_dataset.txt` | Official Rosalind sample input |

## Note on data
The dataset submitted to and accepted by Rosalind is unique to each user's account. Only the official sample dataset is included here; the personal dataset and its output are intentionally omitted.

