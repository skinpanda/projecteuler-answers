# Title: Largest product in a series

import os

# Open file containing data

file = open(os.getcwd()+"/resources/euler", "r")
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
