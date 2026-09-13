"""
Rosalind Problem: FIB - Rabbits and Recurrence Relations

Given: Positive integers n <= 40 and k <= 5.
Return: The total number of rabbit pairs present after n months, given that
we begin with 1 pair and that each pair of reproduction-age rabbits produces
a litter of k rabbit pairs (instead of only 1 pair, as in the classic
Fibonacci story).
"""


def fib_rabbits(n: int, k: int) -> int:
    """
    Compute the number of rabbit pairs alive after n months.

    Parameters
    ----------
    n : int
        The number of months to simulate.
    k : int
        The litter size — how many new pairs each mature (reproduction-age)
        pair produces every month.

    Returns
    -------
    int
        The total number of rabbit pairs after n months.

    Recurrence used
    ----------------
    F(n) = F(n-1) + k * F(n-2)
    F(1) = F(2) = 1

    Why this formula works:
      - F(n-1) counts every pair that was already alive last month.
        Rabbits never die in this problem, so all of them are still here.
      - k * F(n-2) counts the newborns this month. Only pairs that were
        already mature TWO months ago (i.e. alive at month n-2) are old
        enough to breed this month, and each such pair contributes k new
        pairs.
    """

    # Base cases: in months 1 and 2 there is just the single starting
    # pair. It isn't mature yet in month 2, so no offspring exist yet.
    if n <= 2:
        return 1

    # Instead of storing the whole sequence in a list (which would use
    # O(n) memory), we only ever need the last two values to compute the
    # next one. So we keep two "rolling" variables:
    #   prev2 -> the value from two months ago, i.e. F(n-2)
    #   prev1 -> the value from one month ago,  i.e. F(n-1)
    prev2, prev1 = 1, 1  # F(1), F(2)

    # Walk forward from month 3 up to month n, updating the pair counts
    # one month at a time.
    for _ in range(3, n + 1):
        # Compute this month's total pairs using the recurrence:
        #   current = (pairs alive last month) + k * (pairs mature enough to breed)
        current = prev1 + k * prev2

        # Slide the two-value window forward by one month:
        #   what was "last month" (prev1) becomes "two months ago" (prev2)
        #   the value we just computed becomes the new "last month" (prev1)
        prev2, prev1 = prev1, current

    # After the loop finishes, prev1 holds F(n) — the answer.
    return prev1


def main():
    # Read n and k from the sample dataset file (two space-separated
    # integers on one line, e.g. "5 3").
    with open("sample_dataset.txt") as f:
        n, k = map(int, f.read().split())

    # Run the calculation and print the result, exactly as Rosalind
    # expects the answer to be submitted.
    result = fib_rabbits(n, k)
    print(result)


# This guard ensures main() only runs when the script is executed
# directly (e.g. `python fib_solution.py`), not when it's imported as a
# module elsewhere.
if __name__ == "__main__":
    main()
