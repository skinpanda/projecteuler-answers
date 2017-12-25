# Title: Longest Collatz Sequence

from Module import Collatz

terms = 0
starting_number = 0

for i in range(999999, 1, -1):
    col_seq = Collatz(i).get_sequence()  # Lists Collatz sequence
    if len(col_seq) > terms:
        terms = len(col_seq)
        starting_number = i

print("Answer: ", starting_number)
