#Write a Python program to make
# combinations of 3 digits.

# Use itertools.combinations to generate all combinations of 3 digits

import itertools
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
combinations = list(itertools.combinations(digits, 3))
for combination in combinations:
    print(combination)