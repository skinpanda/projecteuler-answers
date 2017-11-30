# Title: Largest product in a series

import os

# Open file containing data

abspath = os.path.abspath(os.path.dirname(__file__))
file = open(abspath + "/resources/problem_8_data.txt", "r")

with file as f:
    number = "".join([num.replace("\n", "") for num in f]) # remove newline character

LargestProduct = 0

for i in range(0, 987):
    prod = 1
    for j in range(i, i + 13):
        prod *= int(number[j])
    if prod > LargestProduct:
        LargestProduct = prod

print("Answer: ", LargestProduct)
