# Rosalind Problem: Rabbits and Recurrence Relations (FIB)

*Rosalind Problem ID:* FIB
*Link:* https://rosalind.info/problems/fib/

## Problem

Fibonacci's rabbits grow in population following a recurrence relation: rabbits reach maturity after one month, and each mature pair produces a litter of k rabbit pairs every subsequent month. The problem asks for the total rabbit pair count after n months.

*Given:* Positive integers n ≤ 40 and k ≤ 5.
*Return:* The total number of rabbit pairs present after n months, if we begin with 1 pair and every mature pair produces a litter of k rabbit pairs (instead of only 1 pair) each generation.

### Sample Dataset
5 3
### Sample Output
19
## Approach

1. Read n (number of months) and k (litter size per mature pair) from the input.
2. Initialize the base cases: F1 = 1, F2 = 1 (one newborn pair in month 1, still one pair — not yet mature — in month 2).
3. Apply the modified recurrence relation: Fn = Fn-1 + k * Fn-2, since new pairs come only from pairs that were already mature two months prior.
4. Iterate from month 3 up to n, building the sequence with a loop (avoids recursion overhead for larger n).
5. Return Fn, the total number of rabbit pairs after n months.

## Files

| File | Description |
|---|---|
| FIB_solution.py | Python solution (reads n and k, applies the modified Fibonacci recurrence, outputs the total pair count) |
| Report_Rabbits_and_Recurrence_Relation.pdf | Full write-up: problem overview, approach, algorithm, complexity analysis, and results |
| 

## Note on data

The dataset submitted to and accepted by Rosalind is unique to each user's account. Only the official sample dataset is included here; the personal dataset and its output are intentionally omitted.
