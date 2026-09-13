# Rosalind Problem: Transcribing DNA into RNA (RNA)

*Rosalind Problem ID:* RNA
*Link:* https://rosalind.info/problems/rna/

## Problem

Given a DNA string, transcribe it into its corresponding RNA string by replacing every occurrence of Thymine (T) with Uracil (U).

*Given:* A DNA string t having length at most 1000 nt.
*Return:* The transcribed RNA string of t.

### Sample Dataset
GATGGAACTTGACTACGTAAATT
### Sample Output
GAUGGAACUUGACUACGUAAAUU
## Approach

1. Read the input DNA string from the file/argument.
2. Iterate through the string and replace every "T" character with "U".
3. Print/write the resulting RNA string.
4. Verify the output length matches the input length (transcription doesn't change length).

## Files

| File | Description |
|---|---|
| RNA_solution.py | Python solution (reads DNA string, replaces T with U, outputs RNA string) |
| Report_on_Transcribing_DNA_into_RNA.pdf | Full write-up: problem overview, approach, algorithm, complexity analysis, and results |

## Note on data

The dataset submitted to and accepted by Rosalind is unique to each user's account. Only the official sample dataset is included here; the personal dataset and its output are intentionally omitted.
